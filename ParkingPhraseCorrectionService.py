import ParkingLibrary


class ParkingPhraseCorrectionService:

    def __init__(self):
        self.parkingLibrary = ParkingLibrary.ParkingLibrary()
        self.levenshtein_threshold = 0.5

    def correct_phrase(self, phrase):
        output_phrases = []
        if phrase.upper() in self.parkingLibrary.parking_vocabulary:
            output_phrases.append(phrase)
        else:
            matched_possible_characters = self.get_matched_possible_characters(phrase)
            character_combinations = self.generate_combinations_of_characters(matched_possible_characters)
            print("RETURNED CHARACTER COMBS: \n" + str(character_combinations))
            # for character_combination in character_combinations:
            #     print("==>> " + character_combination)
            for character_combination in character_combinations:
                if character_combination.upper() in self.parkingLibrary.parking_vocabulary:
                    output_phrases.append(character_combination.upper())

            if len(output_phrases) == 0:
                for character_combination in character_combinations:
                    for parking_phrase in self.parkingLibrary.parking_vocabulary:
                        levenshtein_distance = self.find_levenshtein_distance(character_combination, parking_phrase)
                        if levenshtein_distance <= (len(phrase) * self.levenshtein_threshold):
                            output_phrases.append(character_combination)
        return output_phrases

    def get_matched_possible_characters(self, phrase):
        matched_possible_characters = []
        for char in phrase:
            matched_possible_characters.append(self.parkingLibrary.possible_characters[char])
            # print(" => " + str(self.parkingLibrary.possible_characters[char]))
        return matched_possible_characters

    def generate_combinations_of_characters(self, matched_possible_characters):

        character_combinations = []
        # TODO: Consider left and right alignments for first and last character in the input phrase
        if len(matched_possible_characters) > 0:

            bottom_combinations = self.generate_combinations_for_alignments_top_or_bottom(matched_possible_characters, self.parkingLibrary.alignments.B.name)
            # print("bottom combinations: " + str(bottom_combinations))

            top_combinations = self.generate_combinations_for_alignments_top_or_bottom(matched_possible_characters, self.parkingLibrary.alignments.T.name)
            # print("top combinations: " + str(top_combinations))

            # combine lists and remove duplicates
            character_combinations = bottom_combinations + list(set(top_combinations) - set(bottom_combinations))
            # print("character combs BEFORE first and last: " + str(character_combinations))

            # First character combinations
            if self.parkingLibrary.alignments.L.name in matched_possible_characters[0].keys():
                first_char_combs = self.generate_combinations_for_alignments_left_or_right(character_combinations, matched_possible_characters[0][self.parkingLibrary.alignments.L.name], self.parkingLibrary.alignments.L.name)
                # print("first_char_combs: " + str(first_char_combs))
                character_combinations.extend(first_char_combs)

            # Last character combinations
            if len(matched_possible_characters) > 1 and self.parkingLibrary.alignments.R.name in matched_possible_characters[len(matched_possible_characters)-1].keys():
                last_char_combs = self.generate_combinations_for_alignments_left_or_right(character_combinations, matched_possible_characters[len(matched_possible_characters) - 1][self.parkingLibrary.alignments.R.name], self.parkingLibrary.alignments.R.name)
                # print("last_char_combs: " + str(last_char_combs))
                character_combinations.extend(last_char_combs)
            # print("character combs AFTER first and last: \n" + str(character_combinations))

        return list(set(character_combinations))  # returning character_combinations may be enough (you don't really need to do list(set(character_combinations)) to remove duplicates)

    def generate_combinations_for_alignments_left_or_right(self, existing_combinations, character_options, alignment):
        combinations = set()
        for existing_combination in existing_combinations:
            comb_length = len(existing_combination)
            if comb_length > 0:
                for character_option in character_options:
                    index = 0
                    if alignment == self.parkingLibrary.alignments.R.name:
                        index = comb_length - 1
                    new_comb = self.replace_char_at_index_by_another_char(existing_combination, index, character_option)
                    combinations.add(new_comb)
        return combinations

    def replace_char_at_index_by_another_char(self, string, index, char):
        return string[:index] + char + string[index + 1:]


    def generate_combinations_for_alignments_top_or_bottom(self, matched_possible_characters, alignment):
        combinations = [""]
        for char in matched_possible_characters:
            char_arr = char[self.parkingLibrary.alignments.C.name].copy()
            if alignment in char:
                char_arr.extend(char[alignment].copy())
            combinations = self.generate_combinations_for_current_characters(combinations, char_arr)
        return combinations

    def generate_combinations_for_current_characters(self, prev_strings, curr_characters):
        new_strings = []
        for prev_string in prev_strings:
            for curr_character in curr_characters:
                new_strings.append(prev_string + curr_character)
        return new_strings

    def find_levenshtein_distance(self, str1, str2):
        pass
        # # str1 => char comb,    str2 => parking vocab
        # prev_arr = list(range(0, len(str2) + 1))
        # curr_arr = list()
        # print("arr: " + str(prev_arr))
        # counter = 1
        # for i in range(len(str1)):
        #     curr_arr.append(counter)
        #     for j in range(len(str2)):
        #         if str1[i] == str2[j]:
        #             pass
        # return 1

p = ParkingPhraseCorrectionService()
print("output : " + str(p.find_levenshtein_distance("ZONE", "ONE")))