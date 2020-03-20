import TemplateBoundingBox


class Templates:
    def __init__(self):
        self.templates = [
            # Template 1
            [
                TemplateBoundingBox.TemplateBoundingBox(0.10, 0.88, 0.84, 0.12, "TOW-AWAY", False, True, True),
                TemplateBoundingBox.TemplateBoundingBox(0.00, 0.59, 1.00, 0.23, "NO STOPPING", False, True, True),
                TemplateBoundingBox.TemplateBoundingBox(0.03, 0.36, 0.96, 0.17, "{}{}{}M TO {}{}{}M", True, True, False),  # 10PM TO 6AM
                TemplateBoundingBox.TemplateBoundingBox(0.11, 0.23, 0.82, 0.10, "EVERYDAY", False, True, True),
                TemplateBoundingBox.TemplateBoundingBox(0.24, 0.10, 0.56, 0.06, "FOR TOWED CARS", False, False, True),
                TemplateBoundingBox.TemplateBoundingBox(0.24, 0.00, 0.59, 0.06, "PHONE {}{}{}-{}{}{}{}", False, False, False),
            ]
            # # Template 2
            # [
            #     TemplateBoundingBox.TemplateBoundingBox(0, 0, 0, 0, "PAY-TO", False, True, True),  # missing correct coordinates
            #     TemplateBoundingBox.TemplateBoundingBox(0.22, 0.58, 0.54, 0.15, "PARK", False, True, True),
            #     TemplateBoundingBox.TemplateBoundingBox(0.02, 0.44, 0.93, 0.11, "{}{}{}M TO {}{}{}M", True, True, False),  # 10AM TO 7PM
            #     TemplateBoundingBox.TemplateBoundingBox(0.06, 0.31, 0.21, 0.06, "ZONE", False, False, True),
            #     TemplateBoundingBox.TemplateBoundingBox(0.34, 0.26, 0.20, 0.16, "3", False, False, False),
            #     TemplateBoundingBox.TemplateBoundingBox(0.64, 0.31, 0.28, 0.06, "PERMIT", False, False, True),
            #     TemplateBoundingBox.TemplateBoundingBox(0.30, 0.17, 0.39, 0.06, "REQUIRED", False, False, True),
            #     TemplateBoundingBox.TemplateBoundingBox(0.19, 0.05, 0.61, 0.09, "EVERYDAY", False, True, True),
            #     TemplateBoundingBox.TemplateBoundingBox(0.01, 0.01, 0.26, 0.02, "{{}}", False, False, False),  # "36 CFR 1004.12"
            #     TemplateBoundingBox.TemplateBoundingBox(0.56, 0.00, 0.40, 0.03, "EXCEPT FEDERAL HOLIDAYS", False, True, True),
            # ]
        ]

