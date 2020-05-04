from skbio.sequence import GrammaredSequence
from skbio.util import classproperty
import skbio.alignment as ska


class SequenceAlignmentService:
    class SignSequence(GrammaredSequence):
        @classproperty
        def degenerate_map(cls):
            return {}

        @classproperty
        def definite_chars(cls):
            return set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.:'/&()$-")

        @classproperty
        def default_gap_char(cls):
            return '*'

        @classproperty
        def gap_chars(cls):
            return set('*,')

    def pairwise_align_and_merge_sequences(self, input1, input2):
        output = []
        if len(input1) > 0 and len(input2) > 0:
            sub_matrix = ska.make_identity_substitution_matrix(4, -2,
                                                               alphabet=self.SignSequence.definite_chars)  # match_score, mismatch_score
            x = self.SignSequence(input1.replace(' ', '*'))
            y = self.SignSequence(input2.replace(' ', '*'))
            alignment, score, start_end_positions = ska.global_pairwise_align(x, y, 2, 0.5,
                                                                              substitution_matrix=sub_matrix)
            # print('score %d' % score)
            # print(str(alignment[0]))
            # print(str(alignment[1]))
            output = self.merge_sequences(str(alignment[0]), str(alignment[1]))

        elif len(input1) > 0 and len(input2) == 0:
            output = []
            for char in input1:
                output.append([char])

        elif len(input2) > 0 and len(input1) == 0:
            output = []
            for char in input2:
                output.append([char])
        else:
            output.append([""])
        return output

    def merge_sequences(self, aligned1, aligned2):
        output = []
        for i in range(len(aligned1)):
            if aligned1[i] == aligned2[i] == "*":
                output.append([" "])
            elif aligned1[i] == aligned2[i]:
                output.append([aligned1[i]])
            elif aligned1[i] == "*":
                output.append([aligned2[i]])
            elif aligned2[i] == "*":
                output.append([aligned1[i]])
            else:
                output.append([aligned1[i], aligned2[i]])
        return output
