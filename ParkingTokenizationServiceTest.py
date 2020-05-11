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
             [],
             [[['PA K', [], [['PARK', [], 1], ['PAY', [], 2]]],
               ['NG',
                [],
                [['NO', [], 0],
                 ['10', ['HOUR_PARKING', 'MINUTES_PARKING'], 1],
                 ['20', ['HOUR_PARKING', 'MINUTES_PARKING'], 1],
                 ['TO', [], 1],
                 ['1', ['HOUR_PARKING', 'MINUTES_PARKING'], 2]]]],
              [['PA K NG', [], [['PARKING', [], 2]]]]]]
        ],
        [
            ["/A.M.", [[['/A.M.', OrderedDict([('7A.M.', 0), ('1A.M.', 1), ('2A.M.', 1), ('1P.M.', 2)])]]]],
            ['/A.M.',
             [],
             [[['/A.M.',
                [],
                [['7A.M.', ['TIME_OF_DAY'], 0],
                 ['1A.M.', ['TIME_OF_DAY'], 1],
                 ['2A.M.', ['TIME_OF_DAY'], 1],
                 ['1P.M.', ['TIME_OF_DAY'], 2]]]]]]
        ]
    ]

    def test(self):
        parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()
        for test_case in self.test_cases:
            actual_tokens = parking_tokenization_service.get_matching_tokens(test_case[0])
            self.assertEqual(test_case[1], actual_tokens)


if __name__ == '__main__':
    unittest.main()
