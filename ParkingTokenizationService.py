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
                elements.append([correction[0], self.get_matching_token_for_word(correction[0]), possible_correction_arr])
            correction_set_arr.append(elements)
        return [input_arr[0], self.get_matching_token_for_word(input_arr[0]), correction_set_arr]

    def get_matching_token_for_word(self, word):
        tokens = set()
        for parking_word_token in ParkingWordToken.ParkingWordToken:
            for regex in parking_word_token.value:
                reg = re.compile(regex)
                regex_matches = list(reg.finditer(word.upper()))
                if len(regex_matches) > 0:
                    tokens.add(parking_word_token.name)
        return sorted(tokens)
