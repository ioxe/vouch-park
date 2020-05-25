class ParkingSignWithTokenAndDistance:
    def __init__(self, sign, levenshtein_distance, token_coverage_length):
        self.sign = sign
        self.levenshtein_distance = levenshtein_distance
        self.token_coverage_length = token_coverage_length
