import unittest
from collections import OrderedDict

import ParkingLineCorrectionService


class ParkingLineCorrectionServiceTest(unittest.TestCase):
    test_cases = [
        ["MON SA",
         [[OrderedDict([('MON', 0), ('1AM', 1), ('2AM', 1), ('10', 2), ('1PM', 2), ('6', 2), ('8', 2), ('9', 2), ('FOR', 2), ('SUN', 2)]), OrderedDict([('8', 1), ('8AM', 1), ('SAT', 1), ('1', 2), ('1AM', 2), ('1ST', 2), ('2', 2), ])]]],
        ["PA K NG",
         [[OrderedDict([('PARK', 1), ('PAY', 2)]), OrderedDict([('NO', 0), ('10', 1), ('20', 1), ('TO', 1), ('1', 2)])],
          [OrderedDict([('PARKING', 2)])]]
         ],
        ["PARK NG",
         [[OrderedDict([('PARK', 0), ('PAY', 2)]), OrderedDict([('NO', 0), ('10', 1), ('20', 1), ('TO', 1), ('1', 2)])],
          [OrderedDict([('PARKING', 1)])]]
         ],
        ["PARKING", [[OrderedDict([('PARKING', 0)])]]],
    ]

    def test(self):
        parkingLineCorrectionService = ParkingLineCorrectionService.ParkingLineCorrectionService()

        for test_case in self.test_cases:
            actual_result = parkingLineCorrectionService.get_line_corrections(test_case[0])
            self.assertEqual(test_case[1], actual_result)


if __name__ == '__main__':
    unittest.main()
