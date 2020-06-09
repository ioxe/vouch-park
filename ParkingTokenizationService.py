import ParkingWordToken
import re
import ParkingTokenizedDomain


class ParkingTokenizationService:

    def get_matching_tokens(self, parking_line_correction_domain):
        parking_tokenized_domain = ParkingTokenizedDomain.ParkingTokenizedDomain()
        parking_tokenized_domain.text = parking_line_correction_domain.text
        parking_tokenized_domain.tokens = self.get_matching_token_for_word(parking_tokenized_domain.text)

        # # line_combination
        line_combinations = []
        for input_line_comb in parking_line_correction_domain.line_combinations:
            line_combination = ParkingTokenizedDomain.ParkingTokenizedDomain.LineCombination()

            for input_part_of_line in input_line_comb.parts_of_line:
                part_of_line = ParkingTokenizedDomain.ParkingTokenizedDomain.LineCombination.PartOfLine()
                part_of_line.text = input_part_of_line.text
                part_of_line.tokens = self.get_matching_token_for_word(part_of_line.text)

                for input_word_correction_text, levenshtein_distance in input_part_of_line.word_corrections.items():
                    word_correction = ParkingTokenizedDomain.ParkingTokenizedDomain.LineCombination.PartOfLine.WordCorrection()
                    word_correction.text = input_word_correction_text
                    word_correction.tokens = self.get_matching_token_for_word(input_word_correction_text)
                    word_correction.levenshtein_distance = levenshtein_distance
                    part_of_line.word_corrections.append(word_correction)
                line_combination.parts_of_line.append(part_of_line)
            line_combinations.append(line_combination)

        parking_tokenized_domain.line_combinations = line_combinations
        return parking_tokenized_domain

    def get_matching_token_for_word(self, word):
        tokens = {}
        for parking_word_token in ParkingWordToken.ParkingWordToken:
            coverage_percent = 0
            for regex in parking_word_token.value:
                reg = re.compile(regex)
                regex_matches = list(reg.finditer(word.upper()))
                if len(regex_matches) > 0:
                    for regex_match in regex_matches:
                        match_indices = regex_match.span()
                        match_length = match_indices[1] - match_indices[0]

                        # # TODO: Decide what is better -> match_length vs coverage
                        tokens[parking_word_token.name] = match_length
                        # coverage_percent = max(round((match_length * 100 / len(word.strip("."))), 2),
                        #                        coverage_percent)  # word.strip(".") because regex doesn't match the period at the end of the word
                        # tokens[parking_word_token.name] = coverage_percent
        return tokens
