import unittest
import HourPickerService
import HourSpec


class HourPickerServiceTest(unittest.TestCase):

    def test_hour_windows(self):
        test_objects = {
            # Scan 1.1
            "NO PARKING": None,
            "11 AM TO 1 P.M.": HourSpec.HourSpec("11:00", "13:00"),
            "2nd and 4th MONDAY": None,
            "OF THE MONTH": None,
            "STREET CLEANING": None,

            # Scan 1.2
            "2 HOUR": None,
            "PARKING": None,
            "7A.M.TO 6 P.M.": HourSpec.HourSpec("07:00", "18:00"),
            "EXCEPT SUNDAYS": None,

            # Scan 2
            "9A.M. TO 11A.M.": HourSpec.HourSpec("09:00", "11:00"),
            "10/02 SSC C&C OF S.F. 3M": None,

            # Scan 3
            "STOPPING": None,
            "02/07/20 - 02/09/20": None,
            "11:30PM - 7:00AM": HourSpec.HourSpec("23:30", "07:00"),
            "Fri, Sat, Sun": None,
            "15TH AVE/TARAVAL ST - ULLOA ST": None,
            "(300 ft.) - Odd": None,
            "Pacific Gas & Electric": None,
            "415-695-3500": None,
            "Permit # 20TOC-00678": None,
            "Temp Occupancy": None,
            "QUESTIONS? 554.5824 (M-F)": None,
            "415.553.1200": None,
            "PUBLIC": None,
            "WORKS": None,

            # Scan 4
            "TOW-AWAY": None,
            "NO STOPPING": None,
            "10PM TO 6AM": HourSpec.HourSpec("22:00", "06:00"),
            "EVERYDAY": None,
            "FOR TOWED CARS": None,
            "PHONE 553-1235": None,
            "C&C of S.F. M. 1/93 3M": None,

            # Scan 5
            "PAY TO": None,
            "PARK": None,
            " 10am to 7pm": HourSpec.HourSpec("10:00", "19:00"),
            "ZONE 3": None,
            "PERMIT": None,
            "REQUIRED": None,
            # "EVERYDAY": None,
            "36 CFR 1004.12": None,
            "Except Federal Holidays": None,

            # My Searches
            "12 NOON TO 2 P.M.": HourSpec.HourSpec("12:00", "14:00"),
            "12 NOON TO 12 MIDNIGHT": HourSpec.HourSpec("12:00", "00:00"), # This wasn't really found

            "NO PARKING 12:01 A.M. TO 2 A.M. TUE THRU THUR STREET CLEANING": HourSpec.HourSpec("00:01", "02:00"),
            "NO PARKING TUE & FRI 2:00 AM TO 6:00 AM": HourSpec.HourSpec("02:00", "06:00"),
            "2 HOUR PARKING ENTIRE BLOCK 8AM TO 6PM EXCEPT SUNDAYS & HOLIDAYS": HourSpec.HourSpec("08:00", "18:00"),
            "NO PARKING 12 NOON TO 2 P.M. 1st and 3rd MONDAY of the month": HourSpec.HourSpec("12:00", "14:00"),
            "TOW-AWAY NO STOPPING 7A.M. TO 9 A.M.": HourSpec.HourSpec("07:00", "09:00"),
        }

        for test_text in test_objects:
            hourPickerService = HourPickerService.HourPickerService()
            actual_hour_spec = hourPickerService.pick_hour_window(test_text.strip().upper())
            expected_hour_spec = test_objects[test_text]

            if expected_hour_spec is not None and actual_hour_spec is not None:
                self.assertEqual(expected_hour_spec.from_hour, actual_hour_spec.from_hour)
                self.assertEqual(expected_hour_spec.to_hour, actual_hour_spec.to_hour)
            elif expected_hour_spec is not None and actual_hour_spec is None:
                self.fail("actual_hour_spec is None")
            elif expected_hour_spec is None and actual_hour_spec is not None:
                self.fail("actual_hour_spec is not None")


if __name__ == '__main__':
    unittest.main()
