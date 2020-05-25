import ParkingWordToken
import re


class ParkingTokenizationService:

    def get_matching_tokens(self, input_arr):
        # print(str(input_arr[0]) + " : " + str(self.get_matching_token_for_word(input_arr[0])))
        correction_set_arr = []
        for correctionSet in input_arr[1]:
            elements = []
            for correction in correctionSet:
                # print("\t" + str(correction[0]) + " : " + str(self.get_matching_token_for_word(correction[0])))
                possible_correction_arr = []
                for key, val in correction[1].items():
                    # print("\t\t" + str(key) + " : " + str(self.get_matching_token_for_word(key)))
                    possible_correction_arr.append([key, self.get_matching_token_for_word(key), val])
                elements.append(
                    [correction[0], self.get_matching_token_for_word(correction[0]), possible_correction_arr])
            correction_set_arr.append(elements)
        return [input_arr[0], self.get_matching_token_for_word(input_arr[0]), correction_set_arr]

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

        sorted_tokens = sorted(tokens.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_tokens
