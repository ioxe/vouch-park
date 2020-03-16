import unittest
import InputRefiningService


class InputRefiningServiceTest(unittest.TestCase):

    def test_input_refining_service(self):
        test_cases = [
            [
                ["2 HOUR", "PARKING", "9 A.M. TO 6 P.M.", "MON THRU FRI", "EXCEPT VEHICLES WITH", "AREA U PERMITS"],
                ["2 HOUR PARKING", "9 A.M. TO 6 P.M.", "MON THRU FRI", "EXCEPT VEHICLES WITH", "EXCEPT AREA U PERMITS"]
            ],
            [  # Scan 1.1
                ["NO", "PARKING", "11 AM TO 1 P.M.", "2nd and 4th MONDAY", "OF THE MONTH", "STREET CLEANING"],
                ["NO PARKING", "11 AM TO 1 P.M.", "2nd and 4th MONDAY", "OF THE MONTH", "STREET CLEANING"]
            ],
            [  # Scan 1.2
                ["2 HOUR PARKING", "7A.M.TO 6 P.M.", "EXCEPT SUNDAYS"],
                ["2 HOUR PARKING", "7A.M.TO 6 P.M.", "EXCEPT SUNDAYS"]
            ],
            [  # Scan 2
                ["NO PARKING", "9A.M.", "TO", "11A.M.", "10/02 SSC C&C OF S.F. 3M"],
                ["NO PARKING", "9A.M. TO 11A.M.", "10/02 SSC C&C OF S.F. 3M"]
            ],
            [  # Scan 2 (variation 1)
                ["NO PARKING", "9A.M. TO", "11A.M.", "10/02 SSC C&C OF S.F. 3M"],
                ["NO PARKING", "9A.M. TO 11A.M.", "10/02 SSC C&C OF S.F. 3M"],
            ],
            [  # Scan 2 (Variation 2)
                ["NO PARKING", "9A.M.", "TO 11A.M.", "10/02 SSC C&C OF S.F. 3M"],
                ["NO PARKING", "9A.M. TO 11A.M.", "10/02 SSC C&C OF S.F. 3M"]
            ],
            [  # Scan 3
                ["STOPPING", "02/07/2020 - 05/09/2020", "11:30PM - 7:00AM", "Fri, Sat, Sun",
                 "15TH AVE/TARAVAL ST - ULLOA ST", "(300 ft.) - Odd",
                 "Pacific Gas & Electric", "415-695-3500", "Permit # 20TOC-00678", "Temp Occupancy",
                 "QUESTIONS? 554.5824 (M-F)", "415.553.1200", "PUBLIC", "WORKS"],
                ["STOPPING", "02/07/2020 - 05/09/2020", "11:30PM - 7:00AM", "Fri, Sat, Sun",
                 "15TH AVE/TARAVAL ST - ULLOA ST", "(300 ft.) - Odd",
                 "Pacific Gas & Electric", "415-695-3500", "Permit # 20TOC-00678", "Temp Occupancy",
                 "QUESTIONS? 554.5824 (M-F)", "415.553.1200", "PUBLIC", "WORKS"]
            ],
            [  # Scan 4
                ["TOW-AWAY", "NO STOPPING", "10PM TO 6AM", "EVERYDAY", "FOR TOWED CARS", "PHONE 553-1235",
                 "C&C of S.F. M. 1/93 3M"],
                ["TOW-AWAY", "NO STOPPING", "10PM TO 6AM", "EVERYDAY", "FOR TOWED CARS", "PHONE 553-1235",
                 "C&C of S.F. M. 1/93 3M"]
            ],
            [  # Scan 5
                ["PAY TO", "PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"],
                ["PAY TO PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"]
            ],
            [  # Scan 5 (variation 1)
                ["PAY", "TO", "PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"],
                ["PAY TO PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"]
            ],
            [  # Scan 5 (variation 2)
                ["PAY", "TO PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"],
                ["PAY TO PARK", " 10am to 7pm", "ZONE 3", "PERMIT", "REQUIRED", "36 CFR 1004.12",
                 "EXCEPT FEDERAL HOLIDAYS"]
            ],
            [  # My searches
                ["2 HOUR PARKING", "ENTIRE BLOCK", "8AM TO 6PM", "EXCEPT SUNDAYS AND HOLIDAYS"],
                ["2 HOUR PARKING", "ENTIRE BLOCK", "8AM TO 6PM", "EXCEPT SUNDAYS AND HOLIDAYS"]
            ]
        ]

        for test_case in test_cases:
            input_refining_service = InputRefiningService.InputRefiningService()
            actual_refined_texts = input_refining_service.refine_input(test_case[0])

            expected_refined_texts = test_case[1]
            if len(expected_refined_texts) != 0 and len(actual_refined_texts) != 0:
                self.assertEqual(expected_refined_texts, actual_refined_texts)


if __name__ == '__main__':
    unittest.main()
