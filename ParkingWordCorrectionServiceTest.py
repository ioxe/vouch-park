import unittest
import ParkingWordCorrectionService


class ParkingWordCorrectionServiceTest(unittest.TestCase):

    def test_parking_word_correction_service(self):
        test_cases = [
            ["ZONE", {"ZONE": 0, "ONE": 1, "MON": 2, "AND": 2, "ANY": 2}],
            ["7ONF", {"ZONE": 1, "ONE": 2, "7AM": 2, "AND": 2, "MON": 2, "OF": 2}],
            ["00A.M.", {"8A.M.": 1, "10A.M.": 1, "6A.M.": 1, "1A.M.": 2, "9A.M.": 2,  "2A.M.": 2, "9P.M.": 2, "8P.M.": 2}],
            ["0A.M.", {"8A.M.": 0, "6A.M.": 0, "1A.M.": 1, "2A.M.": 1, "8P.M.": 1, "9A.M.": 1, "9P.M.": 1, "1P.M.": 2}],
            ["HOLD", {"HOUR": 2, "TO": 2, "10": 2, "SAT": 2}],
            ["(A.M.", {"7A.M.": 0, "1A.M.": 1, "2A.M.": 1, "1P.M.": 2}],
            ["/A.M.", {"7A.M.": 0, "1A.M.": 1, "2A.M.": 1, "1P.M.": 2}],
            ["NI", {"NO": 1, "1": 1, "2ND": 1, "AND": 1, "11": 1, "ANY": 1, "OF": 1, "ONE": 1}],
            ["co", {"6": 1, "NO": 1, "TO": 1, "OF": 1, "9": 1, "10": 1, "20": 1, "8": 1, "1": 2, "2": 2, "1AM": 2}],
            ["IONTH", {"MONTH": 0, "MON": 2}],
            ["STORTING", {"STOPPING": 2}],
            ["PA K G", {"PARK": 3, "PARKING": 3}],

            # Incorrect
            # ["nuts P.M.", {"8P.M.": 4, "10P.M.": 4, "10:30P.M.": 4}],
            # ["A.M.", {"1A.M.": 1, "2A.M.": 1, "8A.M.": 1, "8P.M.": 1, "1P.M.": 2}],


        ]

        parking_phrase_correction_service = ParkingWordCorrectionService.ParkingWordCorrectionService()
        for test_case in test_cases:
            expected_phrases = test_case[1]
            actual_phrases = parking_phrase_correction_service.correct_word(test_case[0])
            self.assertEqual(expected_phrases, actual_phrases)


if __name__ == '__main__':
    unittest.main()
