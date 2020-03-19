import BoundingBox


class Template:
    def __init__(self):
        self.templates = [
            [   # Template 1
                [
                    BoundingBox.BoundingBox(0.14, 0.84, 0.73, 0.10, "TOW-AWAY", True),
                    BoundingBox.BoundingBox(0.05, 0.60, 0.87, 0.19, "NO STOPPING", True),
                    BoundingBox.BoundingBox(0.08, 0.41, 0.83, 0.14, "{}{}{}M TO {}{}{}M", True),  # 10PM TO 6AM
                    BoundingBox.BoundingBox(0.15, 0.30, 0.71, 0.08, "EVERYDAY", True),
                    BoundingBox.BoundingBox(0.26, 0.19, 0.49, 0.05, "FOR TOWED CARS", False),
                    BoundingBox.BoundingBox(0.26, 0.11, 0.51, 0.05, "PHONE {}{}{}-{}{}{}{}", False),
                ],

                # Template 2
                [
                    BoundingBox.BoundingBox(0, 0, 0, 0, "PAY-TO", True),  # missing correct coordinates
                    BoundingBox.BoundingBox(0.22, 0.58, 0.54, 0.15, "PARK", True),
                    BoundingBox.BoundingBox(0.02, 0.44, 0.93, 0.11, "{}{}{}M TO {}{}{}M", True),  # 10AM TO 7PM
                    BoundingBox.BoundingBox(0.06, 0.31, 0.21, 0.06, "ZONE", False),
                    BoundingBox.BoundingBox(0.34, 0.26, 0.20, 0.16, "3", False),
                    BoundingBox.BoundingBox(0.64, 0.31, 0.28, 0.06, "PERMIT", False),
                    BoundingBox.BoundingBox(0.30, 0.17, 0.39, 0.06, "REQUIRED", False),
                    BoundingBox.BoundingBox(0.19, 0.05, 0.61, 0.09, "EVERYDAY", True),
                    BoundingBox.BoundingBox(0.01, 0.01, 0.26, 0.02, "{{}}", False),  # "36 CFR 1004.12"
                    BoundingBox.BoundingBox(0.56, 0.00, 0.40, 0.03, "EXCEPT FEDERAL HOLIDAYS", True),
                ],
            ]
        ]
