import unittest
import ParkingPhraseCorrectionService


class ParkingPhraseCorrectionServiceTest(unittest.TestCase):

    def test_parking_correction_service(self):
        test_cases = [
            ["ZONE", {"ZONE": 0, "ONE": 1, "MON": 2}],
            ["7ONF", {"ZONE": 0, "ONE": 1, "MON": 2, "NO": 2, "OF": 2, "TUE": 2}],
            ["ONF", {"ONE": 0, "ZONE": 1, "OF": 1, "2ND": 2, "AND": 2, "9": 2, "6": 2}],
        ]

        parking_phrase_correction_service = ParkingPhraseCorrectionService.ParkingPhraseCorrectionService()
        for test_case in test_cases:
            expected_phrases = test_case[1]
            actual_phrases = parking_phrase_correction_service.correct_phrase(test_case[0])
            self.assertEqual(expected_phrases, actual_phrases)


if __name__ == '__main__':
    unittest.main()
