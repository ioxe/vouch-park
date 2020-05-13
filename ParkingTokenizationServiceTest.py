import unittest
from collections import OrderedDict
import ParkingTokenizationService


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
                 ['10', {'HOUR_PARKING': 100.0, 'MINUTES_PARKING': 100.0}, 1],
                 ['20', {'HOUR_PARKING': 100.0, 'MINUTES_PARKING': 100.0}, 1],
                 ['TO', {'RANGE': 100.0}, 1],
                 ['1', {'HOUR_PARKING': 100.0}, 2]]]],
              [['PA K NG', {}, [['PARKING', {}, 2]]]]]]
        ],
        [
            ["/A.M.", [[['/A.M.', OrderedDict([('7A.M.', 0), ('1A.M.', 1), ('2A.M.', 1), ('1P.M.', 2)])]]]],
            ['/A.M.',
             {},
             [[['/A.M.',
                {},
                [['7A.M.', {'TIME_OF_DAY': 100.0}, 0],
                 ['1A.M.', {'TIME_OF_DAY': 100.0}, 1],
                 ['2A.M.', {'TIME_OF_DAY': 100.0}, 1],
                 ['1P.M.', {'TIME_OF_DAY': 100.0}, 2]]]]]]
        ],
        [
            ["MON SA",
             [[["MON", OrderedDict(
                 [('MON', 0), ('1AM', 1), ('2AM', 1), ('10', 2), ('1PM', 2), ('6', 2), ('8', 2), ('9', 2), ('FOR', 2),
                  ('SUN', 2)])],
               ["SA", OrderedDict([('8', 1), ('8AM', 1), ('SAT', 1), ('1', 2), ('1AM', 2), ('1ST', 2), ('2', 2)])]]]],
            ['MON SA',
             {'DAY_OF_WEEK': 50.0},
             [[['MON',
                {'DAY_OF_WEEK': 100.0},
                [['MON', {'DAY_OF_WEEK': 100.0}, 0],
                 ['1AM', {'TIME_OF_DAY': 100.0}, 1],
                 ['2AM', {'TIME_OF_DAY': 100.0}, 1],
                 ['10', {'HOUR_PARKING': 100.0, 'MINUTES_PARKING': 100.0}, 2],
                 ['1PM', {'TIME_OF_DAY': 100.0}, 2],
                 ['6', {'HOUR_PARKING': 100.0}, 2],
                 ['8', {'HOUR_PARKING': 100.0}, 2],
                 ['9', {'HOUR_PARKING': 100.0}, 2],
                 ['FOR', {}, 2],
                 ['SUN', {'DAY_OF_WEEK': 100.0}, 2]]],
               ['SA',
                {},
                [['8', {'HOUR_PARKING': 100.0}, 1],
                 ['8AM', {'TIME_OF_DAY': 100.0}, 1],
                 ['SAT', {'DAY_OF_WEEK': 100.0}, 1],
                 ['1', {'HOUR_PARKING': 100.0}, 2],
                 ['1AM', {'TIME_OF_DAY': 100.0}, 2],
                 ['1ST', {'WEEK_OF_MONTH': 100.0}, 2],
                 ['2', {'HOUR_PARKING': 100.0}, 2]]]]]]
        ]
    ]

    def test(self):
        parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()
        for test_case in self.test_cases:
            actual_tokens = parking_tokenization_service.get_matching_tokens(test_case[0])
            self.assertEqual(test_case[1], actual_tokens)


if __name__ == '__main__':
    unittest.main()
