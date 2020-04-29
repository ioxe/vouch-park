import unittest
import SequenceAlignmentService


class SequenceAlignmentServiceTest(unittest.TestCase):
    test_cases = [
        [
            ["", ""],
            [[""]]
        ],
        [
            ["BLAH", ""],
            [["B"], ["L"], ["A"], ["H"]]
        ],
        [
            ["", "BLAH"],
            [["B"], ["L"], ["A"], ["H"]]
        ],
        [
            ["SEQUENCE ABC", "QUENCE PBJ"],
            [['S'], ['E'], ['Q'], ['U'], ['E'], ['N'], ['C'], ['E'], [' '], ['A', 'P'], ['B'], ['J'], ['C']]
        ],
        [
            ["HOUR,PARKING,7A.M. TO 6P.,EXCEPT SUNDAYS", "HOUR,PARKING,oP. (A.M.TO,EXCEPT SUNDAYS"],
            [['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','], ['o'], ['P'], [',', '.'], ['7'], ['('], ['A'], ['.'], ['M'], ['.'], [' '], ['T'], ['O'], [','], ['6'], ['P'], ['.'], [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U'], ['N'], ['D'], ['A'], ['Y'], ['S']]
        ],
        [
            ["HOUR,PARKING,oP. (A.M.TO,EXCEPT SUNDAYS", "2 HOUR,PARKING,7A. M.TO 6 P.M.,EXCEPT SUNDAYS"],
            [['2'], [' '], ['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','],
             ['o'], ['P'], ['.'], ['7'], ['('], ['A'], ['.'], [' '], ['M'], ['.'], ['T'], ['O'], [' '], ['6'], [' '],
             ['P'], ['.'], ['M'], ['.'], [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U'], ['N'],
             ['D'], ['A'], ['Y'], ['S']]
        ],
    ]

    def test(self):
        sequence_Alignment_Service = SequenceAlignmentService.SequenceAlignmentService()

        for test_case in self.test_cases:
            actual_output = sequence_Alignment_Service.pairwise_align_and_merge_sequences(test_case[0][0],
                                                                                          test_case[0][1])
            self.assertEqual(test_case[1], actual_output)


if __name__ == '__main__':
    unittest.main()
