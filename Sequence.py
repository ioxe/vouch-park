import argparse
import difflib
import os
import re
import numpy as np

from skbio.sequence import GrammaredSequence
from skbio.util import classproperty
import skbio.alignment as ska
import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class SignSequence(GrammaredSequence):
    @classproperty
    def degenerate_map(cls):
        return {}

    @classproperty
    def definite_chars(cls):
        return set(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,\\/:#&?()'-")

    @classproperty
    def default_gap_char(cls):
        return '*'

    @classproperty
    def gap_chars(cls):
        return set('*;')


def normalize(raw_input):
    flattened = raw_input.replace(';', ' ')
    # special case '-' as it requires escaping unless first or last :-(
    definite_chars = SignSequence.definite_chars
    definite_chars.remove('-')
    p = re.compile(r'[^%s-]' % definite_chars)
    allowed_chars = p.sub('', flattened)
    return allowed_chars


def align(raw_a: str, raw_b: str):
    a = SignSequence(normalize(raw_a))
    b = SignSequence(normalize(raw_b))
    sub_matrix = ska.make_identity_substitution_matrix(4, -2, alphabet=SignSequence.definite_chars)  # match_score, mismatch_score
    alignment, score, start_end_positions = ska.global_pairwise_align(a, b, 4, 1, substitution_matrix=sub_matrix)
    print(str(alignment[0]))
    print(str(alignment[1]))
    print('alignment score %d (higher == better alignment)' % score)
    print('hamming distance %.2f%% (lower == fewer mismatches)' % alignment[0].distance(alignment[1]))
    return alignment[0], alignment[1], alignment[0].distance(alignment[1])


def rearrange(a: str, b: str):
    s = difflib.SequenceMatcher(lambda x: x in ['*'], a, b)
    for block in s.get_matching_blocks():
        if block.a != block.b and block.size > 3:
            print("rearrange %s" % s.a[block.a:block.a + block.size])


def wer(sample: str, label: str):
    aligned_sample, aligned_label, distance = align(sample, label)
    # diff_only_sample = ''
    # sample_index = 0
    rearrange(aligned_sample._string, aligned_label._string)
    rearrange(aligned_label._string, aligned_sample._string)
    # else:
    #     diff_only_sample += s.a[sample_index:block.a]
    #     sample_index = block.a + block.size
    # print(ssl.ratio())
    return


def matched_tokens(a, b):
    """ matches each unigram in a to b
    spacing in a is normalized to match b
    """
    a_grams = a.split()
    b_grams = b.split()

    matched_list = []
    missed_list = []
    a_gram: str
    a_index: int
    for a_index, a_gram in enumerate(a_grams):
        matches = process.extract(a_gram, b_grams, scorer=fuzz.token_sort_ratio)
        matched = False
        for b_gram, score in matches:
            if score > 80:
                matched_list.append(a_gram)
                matched = True
                break
            b_index = b_grams.index(b_gram)
            if score >= 50:
                remainder = a_gram.replace(b_gram, '')
                if remainder != a_gram:
                    # matched a substring
                    # if next gram is a match too, 'a' is missing a space vs. 'b'
                    if b_index+1 < len(b_grams) and remainder == b_grams[b_index+1]:
                        print("\"%s\" elision match found %s+%s" % (a_gram, b_gram, remainder))
                        # a_grams[a_index] = b_gram
                        # a_grams.insert(a_index+1, remainder)
                        # return matched_tokens(' '.join(a_grams), ' '.join(b_grams))
                    else:
                        print("\"%s\" partial match candidate %s (remainder %s)" % (a_gram, b_gram, remainder))
                        print(matches)
                else:
                    # extra space
                    if a_index+1 < len(a_grams) and a_gram + a_grams[a_index+1] == b_gram:
                        print("\"%s\" separation match found %s (target %s)" % (a_gram, a_grams[a_index+1], b_gram))
                        # a_grams[a_index] = b_gram
                        # del a_grams[a_index+1]
                        # return matched_tokens(' '.join(a_grams), ' '.join(b_grams))
        if not matched:
            missed_list.append(a_gram)
    return ' '.join(a_grams), matched_list, missed_list

#
# compute bag-of-words error rate to accommodate multiple orderings of temporary sign text
#
labelDict = {}
styles = []
imageids = []
parser = argparse.ArgumentParser()
parser.add_argument('dbfile')
args = parser.parse_args()
conn = sqlite3.connect(os.path.expanduser(args.dbfile))
c = conn.cursor()
for row in c.execute("SELECT imageid, label FROM images;"):
    labelDict[row[0]] = row[1]
for row in c.execute("SELECT DISTINCT style from samples;"):
    styles.append(row[0])
# compare styles with each other
# for row in c.execute("SELECT DISTINCT imageid FROM samples;"):
#     imageids.append(row[0])
# for imageid in imageids:
#     for row in c.execute("SELECT text FROM samples WHERE imageid=? AND style=?;", (imageid, 'MLKit Cloud (sparse)',)):
#         sample_a = row[0]
#     for row in c.execute("SELECT text FROM samples WHERE imageid=? AND style=?;", (imageid, 'VNRecognizeText',)):
#         sample_b = row[0]
#     align(sample_a, sample_b)

bag_of_words_scores = {}
# compare each style with label
for style in styles:
    bag_of_words_scores[style] = []
    print("-- %s --" % style)
    for row in c.execute("SELECT imageid, text FROM samples WHERE style=?;", (style,)):
        sample = row[1].replace(';', ' ')
        label = labelDict[row[0]].replace(';', ' ')
        aligned_sample_sequence, aligned_label_sequence, hd = align(sample, label)
        aligned_sample = aligned_sample_sequence._string.decode("utf-8")
        aligned_label = aligned_label_sequence._string.decode("utf-8")
        # remove spacing placeholders
        normalized_sample = ''
        for index, _ in enumerate(aligned_label):
            if aligned_sample[index] == '*' and aligned_label[index] == ' ':
                normalized_sample += ' '  # add space to sample
            elif aligned_sample[index] == ' ' and aligned_label[index] == '*' and \
                    ((index-1 < 0 or aligned_label[index-1] != '*') and
                     (index+1 >= len(aligned_label) or aligned_label[index+1] != '*')):
                continue  # remove space from sample
            else:
                normalized_sample += aligned_sample[index]  # pass through
        # remove mismatch placeholders
        normalized_sample = normalized_sample.replace('*', '')
        _, matches, mismatches = matched_tokens(normalized_sample, label)
        score = fuzz.token_sort_ratio(normalized_sample, label)
        bag_of_words_scores[style].append(score)
        print("[%d] %s" % (row[0], sample))
        print("[%d] %s" % (row[0], aligned_sample))
        print("[%d] %s" % (row[0], normalized_sample))
        print("[%d] %s" % (row[0], label))
        print("[%d] (%f) %s, %s" % (row[0], score, matches, mismatches))
        # _, _, hamming_distance = align(row[1], labelDict[row[0]])
        # hamming_sum += hamming_distance
conn.close()

for style in styles:
    scores = np.asarray(bag_of_words_scores[style])
    print("min %2.0f max %2.0f mean %2.1f %s" % (scores.min(), scores.max(), scores.mean(), style))  # = bag_of_words_score / sample_count
#for (style, score) in styles.items():
#    print("-- %f score %s --" % (score, style))

# now measure levenshtein distance post alignment?

# try MSA with all 3 OCR results?

# local alignment drops mismatches at head and tail
# alignment, score, start_end_positions = ska.local_pairwise_align(pred_a, label, 2, 0.5, substitution_matrix=sub_matrix)
# print(str(alignment[0]))
# print(str(alignment[1]))
# print(start_end_positions)
# print('score %d' % score)
