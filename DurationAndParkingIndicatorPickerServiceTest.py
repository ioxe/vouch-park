import unittest
import DurationAndParkingIndicatorPickerService


class DurationAndParkingIndicatorPickerServiceTest(unittest.TestCase):

    def test_duration_and_parking_indicator(self):
        test_objects = {
            # Scan 1.1
            "NO PARKING": [0, 0],

            # Scan 1.2
            "2 HOUR PARKING": [2, 1],

            # Scan 3
            "STOPPING": [0, 0],

            # Scan 4
            "TOW-AWAY": [0, 0],

            # Scan 5
            "PAY TO PARK": [0, 2],

            "NO PARKING 12:01 A.M. TO 2 A.M. TUE THRU THUR STREET CLEANING": [0, 0],
            "NO PARKING TUE & FRI 2:00 AM TO 6:00 AM": [0, 0],
            "10 HOUR PARKING ENTIRE BLOCK 8AM TO 6PM EXCEPT SUNDAYS & HOLIDAYS": [10, 1],
            "NO PARKING 12 NOON TO 2 P.M. 1st and 3rd MONDAY of the month": [0, 0],
            "TOW-AWAY NO STOPPING 7A.M. TO 9 A.M.": [0, 0],
        }

        duration_and_parking_indicator_picker_service = DurationAndParkingIndicatorPickerService.DurationAndParkingIndicatorPickerService()

        for test_object in test_objects:
            expected_duration_and_parking_indicator = test_objects[test_object]
            actual_duration_and_parking_indicator = duration_and_parking_indicator_picker_service.pick_duration_and_parking_indicator(
                test_object)

            self.assertEqual(expected_duration_and_parking_indicator[0], actual_duration_and_parking_indicator[0])
            self.assertEqual(expected_duration_and_parking_indicator[1], actual_duration_and_parking_indicator[1])


if __name__ == '__main__':
    unittest.main()
