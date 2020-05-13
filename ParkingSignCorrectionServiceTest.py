import unittest
import ParkingSignCorrectionService


class ParkingSignCorrectionServiceTest(unittest.TestCase):
    # TODO: Work in progress
    test_cases = [
        [
            ["HOUR,PARKING,7A.M. TO 6P.,EXCEPT SUNDAYS", "HOUR,PARKING,oP. (A.M.TO,EXCEPT SUNDAYS"],
            []
        ]
    ]

    def test(self):
        parking_sign_correction_service = ParkingSignCorrectionService.ParkingSignCorrectionService()

        for test_case in self.test_cases:
            actual_result = parking_sign_correction_service.correct_parking_sign(test_case[0])
            # self.assertEqual(test_case[1], actual_result)


if __name__ == '__main__':
    unittest.main()
