import unittest
import DatePickerService
import DateSpec
import datetime


class DatePickerServiceTest(unittest.TestCase):

    def test_date_picker(self):
        date_picker_service = DatePickerService.DatePickerService()

        from_date = datetime.date(2020, 2, 7)
        to_date = datetime.date(2020, 12, 9)
        today = datetime.date.today()
        expected_dates = []
        for i in range(365):
            date_to_evaluate = today + datetime.timedelta(days=i)
            if from_date <= date_to_evaluate <= to_date:
                expected_dates.append(date_to_evaluate.__str__())

        test_objects = {
            "2 HOUR PARKING": None,
            "9 A.M. TO 6 P.M.": None,
            "MON THRU FRI": None,
            "EXCEPT VEHICLES WITH": None,
            "AREA U PERMITS": None,

            # Scan 1.1
            "NO PARKING": None,
            "11 AM TO 1 P.M.": None,
            "2nd and 4th MONDAY": None,
            "OF THE MONTH": None,
            "STREET CLEANING": None,

            # Scan 1.2
            "2 HOUR": None,
            "PARKING": None,
            "7A.M.TO 6 P.M.": None,
            "EXCEPT SUNDAYS": None,

            # Scan 2
            "9A.M. TO 11A.M.": None,
            "10/02 SSC C&C OF S.F. 3M": None,

            # Scan 3
            "STOPPING": None,
            "02/07/2020 - 12/09/2020": DateSpec.DateSpec(False, expected_dates),
            "11:30PM - 7:00AM": None,
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
            "10PM TO 6AM": None,
            "EVERYDAY": None,
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
            "36 CFR 1004.12": None,
            "EXCEPT FEDERAL HOLIDAYS": DateSpec.DateSpec(True, date_picker_service.us_federal_holidays),

            # My searches
            "2 HOUR PARKING ENTIRE BLOCK 8AM TO 6PM EXCEPT SUNDAYS AND HOLIDAYS": DateSpec.DateSpec(True, date_picker_service.us_holidays),
        }

        for test_text in test_objects:

            actual_date_spec = date_picker_service.pick_dates(test_text)
            expected_date_spec = test_objects[test_text]

            if expected_date_spec is not None and actual_date_spec is not None:
                self.assertEqual(expected_date_spec.except_flag, actual_date_spec.except_flag)
                self.assertEqual(expected_date_spec.dates, actual_date_spec.dates)
            elif expected_date_spec is not None and actual_date_spec is None:
                self.fail("actual_weekday_spec is None")
            elif expected_date_spec is None and actual_date_spec is not None:
                self.fail("actual_weekday_spec is not None")


if __name__ == '__main__':
    unittest.main()
