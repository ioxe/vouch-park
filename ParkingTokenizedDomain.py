class ParkingTokenizedDomain:

    class LineCombination:

        class PartOfLine:

            class WordCorrection:
                def __init__(self):
                    self.text = ""
                    self.tokens = {}
                    self.levenshtein_distance = 0

            def __init__(self):
                self.text = ""
                self.tokens = {}
                self.word_corrections = []

        def __init__(self):
            self.parts_of_line = []

    def __init__(self):
        self.text = ""
        self.tokens = {}
        self.line_combinations = []
