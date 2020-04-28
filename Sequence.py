from skbio.sequence import GrammaredSequence
from skbio.util import classproperty
import skbio.alignment as ska


class SignSequence(GrammaredSequence):
    @classproperty
    def degenerate_map(cls):
        return {}

    @classproperty
    def definite_chars(cls):
        return set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./&(")

    @classproperty
    def default_gap_char(cls):
        return '*'

    @classproperty
    def gap_chars(cls):
        return set('*,')

raw_pred_a = "HOUR,PARKING,7A.M. TO 6P.,EXCEPT SUNDAYS,S.F. 3 M,11/98 SSC c&c".upper()
pred_a = SignSequence(raw_pred_a.replace(' ', '*'))
raw_pred_b = "HOUR,PARKING,oP. (A.M.TO,EXCEPT SUNDAYS,S.F. 3 M,11/98 SSC C&C".upper()
pred_b = SignSequence(raw_pred_b.replace(' ', '*'))
raw_pred_c = "2 HOUR,PARKING,7A. M.TO 6 P.M.,EXCEPT SUNDAYS"
pred_c = SignSequence(raw_pred_c.replace(' ', '*'))
raw_label = "2 HOUR,PARKING,7A.M. TO 6P.M.,EXCEPT SUNDAYS,11/98 SSC C&C OF S.F. 3M"
label = SignSequence(raw_label.replace(' ', '*'))
print('OCR a: %s' % raw_pred_a)
print('OCR b: %s' % raw_pred_b)
print('OCR c: %s' % raw_pred_c)
print('label: %s' % raw_label)
sub_matrix = ska.make_identity_substitution_matrix(4, -2, alphabet=SignSequence.definite_chars) # match_score, mismatch_score
for (x, y) in [(pred_a, pred_b), (pred_a, pred_c), (pred_a, label), (pred_b, label), (pred_c, label)]:
    alignment, score, start_end_positions = ska.global_pairwise_align(x, y, 2, 0.5, substitution_matrix=sub_matrix)
    print(str(alignment[0]))
    print(str(alignment[1]))
    print('score %d' % score)

# try MSA with all 3 OCR results?

# local alignment drops mismatches at head and tail
# alignment, score, start_end_positions = ska.local_pairwise_align(pred_a, label, 2, 0.5, substitution_matrix=sub_matrix)
# print(str(alignment[0]))
# print(str(alignment[1]))
# print(start_end_positions)
# print('score %d' % score)