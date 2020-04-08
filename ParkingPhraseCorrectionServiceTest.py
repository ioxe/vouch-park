import unittest
import ParkingPhraseCorrectionService


class ParkingPhraseCorrectionServiceTest(unittest.TestCase):

    def test_parking_correction_service(self):
        test_cases = [
            # ["ZONE", ["ZONE"]],
            # ["7ONF", ["ZONE"]],
            ["ONF", ["ZONE", "ONE"]]
        ]

        parking_phrase_correction_service = ParkingPhraseCorrectionService.ParkingPhraseCorrectionService()
        for test_case in test_cases:
            expected_phrases = test_case[1]
            actual_phrases = parking_phrase_correction_service.correct_phrase(test_case[0])
            self.assertEqual(expected_phrases, actual_phrases)


if __name__ == '__main__':
    unittest.main()
