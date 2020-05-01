import argparse
import os
import re

from skbio.sequence import GrammaredSequence
from skbio.util import classproperty
import skbio.alignment as ska
import sqlite3

class SignSequence(GrammaredSequence):
    @classproperty
    def degenerate_map(cls):
        return {}

    @classproperty
    def definite_chars(cls):
        return set(" ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,/:#&?()'-")

    @classproperty
    def default_gap_char(cls):
        return '*'

    @classproperty
    def gap_chars(cls):
        return set('*;')


def normalize(raw_input):
    flattened = raw_input.upper().replace(';', ' ')
    p = re.compile(r'[^%s]' % SignSequence.definite_chars)
    allowed_chars = p.sub('', flattened)
    return allowed_chars#.replace(' ', '*')


def align(raw_a: str, raw_b: str):
    a = SignSequence(normalize(raw_a))
    b = SignSequence(normalize(raw_b))
    sub_matrix = ska.make_identity_substitution_matrix(4, -2, alphabet=SignSequence.definite_chars)  # match_score, mismatch_score
    alignment, score, start_end_positions = ska.global_pairwise_align(a, b, 4, 1, substitution_matrix=sub_matrix)
    print(str(alignment[0]))
    print(str(alignment[1]))
    print('alignment score %d (higher == better alignment)' % score)
    print('hamming distance %.2f%% (lower == fewer mismatches)' % alignment[0].distance(alignment[1]))
    return alignment[0].distance(alignment[1])


labelDict = {}
parser = argparse.ArgumentParser()
parser.add_argument('dbfile')
args = parser.parse_args()
conn = sqlite3.connect(os.path.expanduser(args.dbfile))
c = conn.cursor()
for row in c.execute("SELECT imageid, label FROM images;"):
    labelDict[row[0]] = row[1]
for style in ['VNRecognizeText',
              'VNDetectTextRectangles followed by VNRecognizeText',
              'Padded VNDetectTextRectangles followed by VNRecognizeText']:
    print("-- %s --" % style)
    sample_count = 0
    hamming_sum = 0
    for row in c.execute("SELECT imageid, text FROM samples WHERE style=?;", (style,)):
        # for sample in row[1].split(";;"):
        hamming_sum += align(row[1], labelDict[row[0]])
        sample_count += 1
    # mean hamming distance per OCR style
    print("-- %s mean %f --" % (style, hamming_sum/sample_count))
conn.close()


# now measure levenshtein distance post alignment?

# try MSA with all 3 OCR results?

# local alignment drops mismatches at head and tail
# alignment, score, start_end_positions = ska.local_pairwise_align(pred_a, label, 2, 0.5, substitution_matrix=sub_matrix)
# print(str(alignment[0]))
# print(str(alignment[1]))
# print(start_end_positions)
# print('score %d' % score)
