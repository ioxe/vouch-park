import unittest
from collections import OrderedDict

import ParkingLineCorrectionService


class ParkingLineCorrectionServiceTest(unittest.TestCase):
    test_cases = [
        ["MON SA",
         [[["MON", OrderedDict(
             [('MON', 0), ('1AM', 1), ('2AM', 1), ('10', 2), ('1PM', 2), ('6', 2), ('8', 2), ('9', 2), ('FOR', 2),
              ('SUN', 2)])],
           ["SA", OrderedDict([('8', 1), ('8AM', 1), ('SAT', 1), ('1', 2), ('1AM', 2), ('1ST', 2), ('2', 2)])]]]],

        ["PA K NG",
         [[["PA K", OrderedDict([('PARK', 1), ('PAY', 2)])], ["NG", OrderedDict([('NO', 0), ('10', 1), ('20', 1), ('TO', 1), ('1', 2)])]],
          [["PA K NG", OrderedDict([('PARKING', 2)])]]]
         ],
        ["PARK NG",
         [
             [["PARK", OrderedDict([('PARK', 0), ('PAY', 2)])],
              ["NG", OrderedDict([('NO', 0), ('10', 1), ('20', 1), ('TO', 1), ('1', 2)])]],
             [["PARK NG", OrderedDict([('PARKING', 1)])]]]
         ],
        ["PARKING", [[["PARKING", OrderedDict([('PARKING', 0)])]]]],

        ["DARKING", [[['DARKING', OrderedDict([('PARKING', 1)])]]]],  # PARKING
        ["STEET", [[['STEET', OrderedDict([('STREET', 1)])]]]],  # STREET
        ["NI", [[['NI', OrderedDict([('1', 1), ('11', 1), ('2ND', 1), ('AND', 1), ('ANY', 1), ('NO', 1), ('OF', 1), ('ONE', 1)])]]]],  # NO

        ["/A.M.", [[['/A.M.', OrderedDict([('7A.M.', 0), ('1A.M.', 1), ('2A.M.', 1), ('1P.M.', 2)])]]]],  # 7 A.M.
        ["$6P.M.", [[['$6P.M.', OrderedDict([('6P.M.', 1), ('1P.M.', 2), ('2P.M.', 2), ('6A.M.', 2)])]]]],  # 6 P.M.
        ["HoUD", [[['HoUD', OrderedDict([('HOUR', 1), ('HOURS', 2)])]]]],  # HOUR


        ["hut", [[['hut', OrderedDict([('HOUR', 1), ('SAT', 1), ('10', 2), ('1AM', 2), ('1ST', 2), ('20', 2), ('2AM', 2), ('FOR', 2), ('SUN', 2), ('THU', 2)])]]]],  # HOUR
        ["EXCEP'.", [[["EXCEP'.", OrderedDict([('EXCEPT', 2)])]]]],  # EXCEPT
        ["PA KING", [[['PA KING', OrderedDict([('PARKING', 1)])]]]],  # PARKING
        ["OP.M.", [[['OP.M.', OrderedDict([('6P.M.', 0), ('8P.M.', 0), ('1P.M.', 1), ('2P.M.', 1), ('8A.M.', 1), ('9A.M.', 1), ('9P.M.', 1), ('1A.M.', 2)])]]]],  # 6P.M.
        ["SU", [[['SU', OrderedDict([('10', 1), ('20', 1), ('8', 1), ('NO', 1), ('SUN', 1), ('TO', 1), ('1', 2), ('1ST', 2), ('2', 2)])]]]],  # SUN

        # Didn't work well enough
        # ["11AMLl1", [[['11AMLl1', OrderedDict([('11AM', 3), ('MINUTE', 3)])]]]],  # 11AM TO 1
        # ["Ho", [[['Ho', OrderedDict([('10', 1), ('20', 1), ('6', 1), ('8', 1), ('9', 1), ('AND', 1), ('NO', 1), ('TO', 1), ('1', 2), ('1AM', 2), ('2', 2)])]]]],  # HOUR
        # ["ho", [[['ho', OrderedDict([('10', 1), ('20', 1), ('6', 1), ('8', 1), ('9', 1), ('NO', 1), ('TO', 1), ('1', 2), ('1AM', 2), ('2', 2)])]]]],  # HOUR
        # ["02/07/20", [[['02/07/20', OrderedDict([('20', 6), ('2A.M.', 6), ('2AM', 6), ('2ND', 6), ('AND', 6), ('AREA', 6), ('TOWED', 6)])]]]],  # 02/07/20
    ]

    def test(self):
        parkingLineCorrectionService = ParkingLineCorrectionService.ParkingLineCorrectionService()

        for test_case in self.test_cases:
            actual_result = parkingLineCorrectionService.get_line_corrections(test_case[0])
            self.assertEqual(test_case[1], actual_result)


if __name__ == '__main__':
    unittest.main()
