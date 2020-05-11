import unittest
import ParkingRuleService
import ParkingRule
import DateSpec
import WeekdaySpec
import HourSpec
import datetime
import DatePickerService


class ParkingRuleServiceTest(unittest.TestCase):

    def test_parking_rule_service(self):
        from_date = datetime.date(2020, 2, 7)
        to_date = datetime.date(2020, 12, 9)
        today = datetime.date.today()
        date_picker_Service = DatePickerService.DatePickerService()
        expected_dates = []
        for i in range(365):
            date_to_evaluate = today + datetime.timedelta(days=i)
            if from_date <= date_to_evaluate <= to_date:
                expected_dates.append(date_to_evaluate.__str__())

        test_case_inputs = {
            1: ["2 HOUR PARKING", "9 A.M. TO 6 P.M.", "MON THRU FRI", "EXCEPT VEHICLES WITH", "AREA U PERMITS"],

            # # Scan 1.1
            2: ["NO PARKING", "11 AM TO 1 P.M.", "2nd and 4th MONDAY", "OF THE MONTH", "STREET CLEANING"],

            # # Scan 1.2
            3: ["2 HOUR PARKING", "7A.M.TO 6 P.M.", "EXCEPT SUNDAYS"],

            # Scan 2
            4: ["NO PARKING", "9A.M. TO 11A.M.", "10/02 SSC C&C OF S.F. 3M"],

            # Scan 3
            5: ["STOPPING", "02/07/2020 - 12/09/2020", "11:30PM - 7:00AM", "Fri, Sat, Sun",
                "15TH AVE/TARAVAL ST - ULLOA ST", "(300 ft.) - Odd",
                "Pacific Gas & Electric", "415-695-3500", "Permit # 20TOC-00678", "Temp Occupancy",
                "QUESTIONS? 554.5824 (M-F)", "415.553.1200", "PUBLIC", "WORKS"],

            # Scan 4
            6: ["TOW-AWAY", "NO STOPPING", "10PM TO 6AM", "EVERYDAY", "FOR TOWED CARS", "PHONE 553-1235",
                "C&C of S.F. M. 1/93 3M"],

            # Scan 5
            7: ["PAY TO PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                "EXCEPT FEDERAL HOLIDAYS"],

            # # My searches
            8: ["2 HOUR PARKING", "ENTIRE BLOCK", "8AM TO 6PM", "EXCEPT SUNDAYS AND HOLIDAYS"]
        }

        test_case_results = {
            1: ParkingRule.ParkingRule(None,
                                       [WeekdaySpec.WeekdaySpec([], [2, 3, 4, 5, 6], [])],
                                       [HourSpec.HourSpec("09:00", "18:00")],
                                       120,
                                       1),

            # Scan 1.1
            2: ParkingRule.ParkingRule(None,
                                       [WeekdaySpec.WeekdaySpec([], [2], [2, 4])],
                                       [HourSpec.HourSpec("11:00", "13:00")],
                                       0,
                                       0),

            # Scan 1.2
            3: ParkingRule.ParkingRule(None,
                                       [WeekdaySpec.WeekdaySpec([], [2, 3, 4, 5, 6, 7], [])],
                                       [HourSpec.HourSpec("07:00", "18:00")],
                                       120,
                                       1),

            # Scan 2
            4: ParkingRule.ParkingRule(None,
                                       [],
                                       [HourSpec.HourSpec("09:00", "11:00")],
                                       0,
                                       0),

            # Scan 3
            5: ParkingRule.ParkingRule([DateSpec.DateSpec(False, expected_dates)],
                                       [WeekdaySpec.WeekdaySpec([], [6, 7, 1], [])],
                                       [HourSpec.HourSpec("23:30", "07:00")],
                                       0,
                                       0),

            # Scan 4
            6: ParkingRule.ParkingRule([],
                                       [WeekdaySpec.WeekdaySpec([], [2, 3, 4, 5, 6, 7, 1],
                                                                [])],
                                       [HourSpec.HourSpec("22:00", "06:00")],
                                       0,
                                       0),

            # Scan 5
            7: ParkingRule.ParkingRule([DateSpec.DateSpec(True, date_picker_Service.us_federal_holidays)],
                                       [],
                                       [HourSpec.HourSpec("10:00", "19:00")],
                                       0,
                                       2),

            # # My searches
            8: ParkingRule.ParkingRule([DateSpec.DateSpec(True, date_picker_Service.us_holidays)],
                                       [WeekdaySpec.WeekdaySpec([], [2, 3, 4, 5, 6, 7], [])],
                                       [HourSpec.HourSpec("08:00", "18:00")],
                                       120,
                                       1),
        }

        for test_case_input in test_case_inputs:
            parking_rule_service = ParkingRuleService.ParkingRuleService()
            actual_parking_rule = parking_rule_service.checkParkingSign(test_case_inputs[test_case_input])

            expected_parking_rule = test_case_results[test_case_input]
            if expected_parking_rule.date_specs is not None and actual_parking_rule.date_specs is not None:
                self.assertEqual(len(expected_parking_rule.date_specs), len(actual_parking_rule.date_specs))
                if len(expected_parking_rule.date_specs) > 0:
                    self.assertEqual(expected_parking_rule.date_specs[0].dates, actual_parking_rule.date_specs[0].dates)
                    self.assertEqual(expected_parking_rule.date_specs[0].except_flag, actual_parking_rule.date_specs[0].except_flag)

            self.assertEqual(len(expected_parking_rule.hour_specs), len(actual_parking_rule.hour_specs))
            if len(expected_parking_rule.hour_specs) > 0:
                self.assertEqual(expected_parking_rule.hour_specs[0].from_hour,
                                 actual_parking_rule.hour_specs[0].from_hour)
                self.assertEqual(expected_parking_rule.hour_specs[0].to_hour, actual_parking_rule.hour_specs[0].to_hour)

            self.assertEqual(len(expected_parking_rule.weekday_specs), len(actual_parking_rule.weekday_specs))
            if len(expected_parking_rule.weekday_specs) > 0:
                self.assertEqual(expected_parking_rule.weekday_specs[0].months,
                                 actual_parking_rule.weekday_specs[0].months)
                self.assertEqual(expected_parking_rule.weekday_specs[0].days_of_week,
                                 actual_parking_rule.weekday_specs[0].days_of_week)
                self.assertEqual(expected_parking_rule.weekday_specs[0].weeks_of_month,
                                 actual_parking_rule.weekday_specs[0].weeks_of_month)
            self.assertEqual(expected_parking_rule.duration_minutes, actual_parking_rule.duration_minutes)
            self.assertEqual(expected_parking_rule.parking_indicator, actual_parking_rule.parking_indicator)


if __name__ == '__main__':
    unittest.main()
