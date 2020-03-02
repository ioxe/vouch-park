import unittest
import WeekdaySpec
import WeekdayPickerService


class WeekdayPickerServiceTest(unittest.TestCase):

    def test_weekday_picker(self):
        test_objects = {

            "2 HOUR PARKING": None,
            "9 A.M. TO 6 P.M.": None,
            "MON THRU FRI": WeekdaySpec.WeekdaySpec([], ["MON", "TUE", "WED", "THU", "FRI"], []),
            "EXCEPT VEHICLES WITH": None,
            "AREA U PERMITS": None,

            # Scan 1.1
            "NO PARKING": None,
            "11 AM TO 1 P.M.": None,
            "2nd and 4th MONDAY": WeekdaySpec.WeekdaySpec([], ["MON"], [2, 4]),
            "OF THE MONTH": None,
            "STREET CLEANING": None,

            # # Scan 1.2
            "2 HOUR": None,
            "PARKING": None,
            "7A.M.TO 6 P.M.": None,
            "EXCEPT SUNDAYS": WeekdaySpec.WeekdaySpec([], ["MON", "TUE", "WED", "THU", "FRI", "SAT"], []),

            # Scan 2
            "9A.M. TO 11A.M.": None,
            "10/02 SSC C&C OF S.F. 3M": None,

            # Scan 3
            "STOPPING": None,
            "02/07/20 - 02/09/20": None,
            "11:30PM - 7:00AM": None,
            "Fri, Sat, Sun": WeekdaySpec.WeekdaySpec([], ["FRI", "SAT", "SUN"], []),
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
            "10PM TO 6AM": None,
            "EVERYDAY": WeekdaySpec.WeekdaySpec([], ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"], []),
            "FOR TOWED CARS": None,
            "PHONE 553-1235": None,
            "C&C of S.F. M. 1/93 3M": None,

            # Scan 5
            "PAY TO": None,
            "PARK": None,
            " 10am to 7pm": None,
            "ZONE 3": None,
            "PERMIT": None,
            "REQUIRED": None,
            # "EVERYDAY": WeekdaySpec.WeekdaySpec([], ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"], []),
            "36 CFR 1004.12": None,
            "EXCEPT FEDERAL HOLIDAYS": None,
        }

        for test_text in test_objects:
            hourPickerService = WeekdayPickerService.WeekdayPickerService()
            actual_weekday_spec = hourPickerService.pick_weekdays(test_text.strip().upper())
            expected_weekday_spec = test_objects[test_text]

            if expected_weekday_spec is not None and actual_weekday_spec is not None:
                self.assertEqual(expected_weekday_spec.days_of_Week, actual_weekday_spec.days_of_Week)
                self.assertEqual(expected_weekday_spec.weeks_of_month, actual_weekday_spec.weeks_of_month)
                self.assertEqual(expected_weekday_spec.months, actual_weekday_spec.months)
            elif expected_weekday_spec is not None and actual_weekday_spec is None:
                self.fail("actual_weekday_spec is None")
            elif expected_weekday_spec is None and actual_weekday_spec is not None:
                self.fail("actual_weekday_spec is not None")


if __name__ == '__main__':
    unittest.main()
