import unittest
from collections import OrderedDict
import ParkingTokenizationService
import ParkingLineCorrectionDomain


class ParkingTokenizationServiceTest(unittest.TestCase):
    test_cases = [
        [
            ["PA K NG",
             [[["PA K", OrderedDict([('PARK', 1), ('PAY', 2)])],
               ["NG", OrderedDict([('NO', 0), ('10', 1), ('20', 1), ('TO', 1), ('1', 2)])]],
              [["PA K NG", OrderedDict([('PARKING', 2)])]]]
             ],
            ['PA K NG',
             {},
             [[['PA K', {}, [['PARK', {}, 1], ['PAY', {}, 2]]],
               ['NG',
                {},
                [['NO', {}, 0],
                 ['10', {'HOUR_PARKING': 2, 'MINUTES_PARKING': 2}, 1],
                 ['20', {'HOUR_PARKING': 2, 'MINUTES_PARKING': 2}, 1],
                 ['TO', {'RANGE': 2}, 1],
                 ['1', {'HOUR_PARKING': 1}, 2]]]],
              [['PA K NG', {}, [['PARKING', {}, 2]]]]]]
        ],
        [
            ["/A.M.", [[['/A.M.', OrderedDict([('7A.M.', 0), ('1A.M.', 1), ('2A.M.', 1), ('1P.M.', 2)])]]]],
            ['/A.M.',
             {},
             [[['/A.M.',
                {},
                [['7A.M.', {'TIME_OF_DAY': 4}, 0],
                 ['1A.M.', {'TIME_OF_DAY': 4}, 1],
                 ['2A.M.', {'TIME_OF_DAY': 4}, 1],
                 ['1P.M.', {'TIME_OF_DAY': 4}, 2]]]]]]
        ],
        [
            ["MON SA",
             [[["MON", OrderedDict(
                 [('MON', 0), ('1AM', 1), ('2AM', 1), ('10', 2), ('1PM', 2), ('6', 2), ('8', 2), ('9', 2), ('FOR', 2),
                  ('SUN', 2)])],
               ["SA", OrderedDict([('8', 1), ('8AM', 1), ('SAT', 1), ('1', 2), ('1AM', 2), ('1ST', 2), ('2', 2)])]]]],
            ['MON SA',
             {'DAY_OF_WEEK': 3},
             [[['MON',
                {'DAY_OF_WEEK': 3},
                [['MON', {'DAY_OF_WEEK': 3}, 0],
                 ['1AM', {'TIME_OF_DAY': 3}, 1],
                 ['2AM', {'TIME_OF_DAY': 3}, 1],
                 ['10', {'HOUR_PARKING': 2, 'MINUTES_PARKING': 2}, 2],
                 ['1PM', {'TIME_OF_DAY': 3}, 2],
                 ['6', {'HOUR_PARKING': 1}, 2],
                 ['8', {'HOUR_PARKING': 1}, 2],
                 ['9', {'HOUR_PARKING': 1}, 2],
                 ['FOR', {}, 2],
                 ['SUN', {'DAY_OF_WEEK': 3}, 2]]],
               ['SA',
                {},
                [['8', {'HOUR_PARKING': 1}, 1],
                 ['8AM', {'TIME_OF_DAY': 3}, 1],
                 ['SAT', {'DAY_OF_WEEK': 3}, 1],
                 ['1', {'HOUR_PARKING': 1}, 2],
                 ['1AM', {'TIME_OF_DAY': 3}, 2],
                 ['1ST', {'WEEK_OF_MONTH': 3}, 2],
                 ['2', {'HOUR_PARKING': 1}, 2]]]]]]
        ]
    ]

    def test(self):
        parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()

        for test_case in self.test_cases:
            parking_line_correction_domain = self.transform_to_parking_line_correction_domain(test_case[0])
            actual_tokens = parking_tokenization_service.get_matching_tokens(parking_line_correction_domain)
            self.verify_results(test_case[1], actual_tokens)

    def transform_to_parking_line_correction_domain(self, input_arr):
        parking_line_correction_domain = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain()
        parking_line_correction_domain.text = input_arr[0]

        line_combinations = []
        for i in range(0, len(input_arr[1])):
            line_combination = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination()

            for j in range(0, len(input_arr[1][i])):
                part_of_line = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination.PartOfLine()
                part_of_line.text = input_arr[1][i][j][0]
                part_of_line.word_corrections = input_arr[1][i][j][1]
                line_combination.parts_of_line.append(part_of_line)
            line_combinations.append(line_combination)

        parking_line_correction_domain.line_combinations = line_combinations
        return parking_line_correction_domain

    def verify_results(self, expected, actual):
        self.assertEqual(expected[0], actual.text)
        self.assertEqual(expected[1], actual.tokens)
        self.assertEqual(len(expected[2]), len(actual.line_combinations))

        # line_combination
        for i in range(0, len(expected[2])):
            # part_of_line
            for j in range(0, len(expected[2][i])):
                self.assertEqual(expected[2][i][j][0], actual.line_combinations[i].parts_of_line[j].text)
                self.assertEqual(expected[2][i][j][1], actual.line_combinations[i].parts_of_line[j].tokens)
                self.assertEqual(len(expected[2][i][j][2]),
                                 len(actual.line_combinations[i].parts_of_line[j].word_corrections))
                # word_correction
                for k in range(0, len(expected[2][i][j][2])):
                    self.assertEqual(expected[2][i][j][2][k][0],
                                     actual.line_combinations[i].parts_of_line[j].word_corrections[k].text)
                    self.assertEqual(expected[2][i][j][2][k][1],
                                     actual.line_combinations[i].parts_of_line[j].word_corrections[k].tokens)
                    self.assertEqual(expected[2][i][j][2][k][2],
                                     actual.line_combinations[i].parts_of_line[j].word_corrections[
                                         k].levenshtein_distance)


if __name__ == '__main__':
    unittest.main()
