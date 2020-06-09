class ParkingLineCorrectionDomain:

    class LineCombination:

        class PartOfLine:
            def __init__(self):
                self.text = ""
                self.word_corrections = []

        def __init__(self):
            self.parts_of_line = []

    def __init__(self):
        self.text = ""
        self.line_combinations = []
