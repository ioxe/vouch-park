import ParkingWordsLibrary
import collections


class ParkingWordCorrectionService:

    def __init__(self):
        self.parking_words_library = ParkingWordsLibrary.ParkingWordsLibrary()
        self.min_levenstein_distance = 2

    def correct_word(self, phrase):
        output_phrases = {}

        # Generate character combinations
        matched_possible_characters = self.get_matched_possible_characters(phrase)
        character_combinations = self.generate_combinations_of_characters(matched_possible_characters)

        # Generate combined_levenshtein_distance_map for each combination
        combined_levenshtein_distance_map = {}
        for character_combination in character_combinations:
            levenshtein_distance_map = self.get_levenshtein_distance_map(character_combination,
                                                                         self.parking_words_library.parking_words_vocabulary)
            # select top n elements (n = self.min_levenstein_distance)
            for i in range(0, self.min_levenstein_distance):
                close_match_key = list(levenshtein_distance_map.keys())[i]  # Select close match
                if close_match_key in combined_levenshtein_distance_map and combined_levenshtein_distance_map[
                    close_match_key] > levenshtein_distance_map[close_match_key]:
                    combined_levenshtein_distance_map[close_match_key] = levenshtein_distance_map[close_match_key]
                elif close_match_key not in combined_levenshtein_distance_map:
                    combined_levenshtein_distance_map[close_match_key] = levenshtein_distance_map[close_match_key]
        sorted_combined_levenshtein_distance_map = collections.OrderedDict(
            sorted(combined_levenshtein_distance_map.items(),
                   key=lambda item: item[1]))
        combined_levenshtein_distance_map_keys = list(sorted_combined_levenshtein_distance_map.keys())

        # determine how many close words to return
        levenshtein_distance_threshold = max(
            sorted_combined_levenshtein_distance_map[combined_levenshtein_distance_map_keys[0]],
            self.min_levenstein_distance)
        for key in combined_levenshtein_distance_map_keys:
            if sorted_combined_levenshtein_distance_map[key] <= levenshtein_distance_threshold:
                output_phrases[key] = sorted_combined_levenshtein_distance_map[key]
        sorted_output_phrases = collections.OrderedDict(sorted(output_phrases.items(), key=lambda item: (item[1], item[0])))
        return sorted_output_phrases

    def get_matched_possible_characters(self, phrase):
        matched_possible_characters = []
        for char in phrase:
            matched_possible_characters.append(self.parking_words_library.possible_characters[char])
            # print(" => " + str(self.parkingLibrary.possible_characters[char]))
        return matched_possible_characters

    def generate_combinations_of_characters(self, matched_possible_characters):

        character_combinations = []
        # TODO: Consider left and right alignments for first and last character in the input phrase
        if len(matched_possible_characters) > 0:

            center_combinations = self.generate_combinations_for_alignments_top_or_bottom_or_center(
                matched_possible_characters,
                self.parking_words_library.alignments.C.name)

            bottom_combinations = self.generate_combinations_for_alignments_top_or_bottom_or_center(
                matched_possible_characters,
                self.parking_words_library.alignments.B.name)

            top_combinations = self.generate_combinations_for_alignments_top_or_bottom_or_center(
                matched_possible_characters,
                self.parking_words_library.alignments.T.name)

            # combine lists and remove duplicates

            character_combinations = list(set(center_combinations + bottom_combinations + top_combinations))

            # First character combinations
            if self.parking_words_library.alignments.L.name in matched_possible_characters[0].keys():
                first_char_combs = self.generate_combinations_for_alignments_left_or_right(character_combinations,
                                                                                           matched_possible_characters[
                                                                                               0][
                                                                                               self.parking_words_library.alignments.L.name],
                                                                                           self.parking_words_library.alignments.L.name)
                character_combinations.extend(first_char_combs)

            # Last character combinations
            if len(matched_possible_characters) > 1 and self.parking_words_library.alignments.R.name in \
                    matched_possible_characters[len(matched_possible_characters) - 1].keys():
                last_char_combs = self.generate_combinations_for_alignments_left_or_right(character_combinations,
                                                                                          matched_possible_characters[
                                                                                              len(
                                                                                                  matched_possible_characters) - 1][
                                                                                              self.parking_words_library.alignments.R.name],
                                                                                          self.parking_words_library.alignments.R.name)
                character_combinations.extend(last_char_combs)

        return list(set(
            character_combinations))  # returning character_combinations may be enough (you don't really need to do list(set(character_combinations)) to remove duplicates)

    def generate_combinations_for_alignments_left_or_right(self, existing_combinations, character_options, alignment):
        combinations = set()
        for existing_combination in existing_combinations:
            comb_length = len(existing_combination)
            if comb_length > 0:
                for character_option in character_options:
                    index = 0
                    if alignment == self.parking_words_library.alignments.R.name:
                        index = comb_length - 1
                    new_comb = self.replace_char_at_index_by_another_char(existing_combination, index, character_option)
                    combinations.add(new_comb)
        return combinations

    def replace_char_at_index_by_another_char(self, string, index, char):
        return string[:index] + char + string[index + 1:]

    def generate_combinations_for_alignments_top_or_bottom_or_center(self, matched_possible_characters, alignment):
        combinations = [""]
        for char in matched_possible_characters:
            # char_arr = char[self.parkingLibrary.alignments.C.name].copy()
            char_arr = []
            if alignment in char:
                char_arr = char[alignment].copy()
            else:
                char_arr = char[self.parking_words_library.alignments.C.name].copy()
            combinations = self.generate_combinations_for_current_characters(combinations, char_arr)

        return combinations

    def generate_combinations_for_current_characters(self, prev_strings, curr_characters):
        new_strings = []
        for prev_string in prev_strings:
            for curr_character in curr_characters:
                new_strings.append(prev_string + curr_character)
        return new_strings

    # def generate_combinations_for_alignments_top_or_bottom(self, matched_possible_characters, alignment):
    #     combinations = [""]
    #     for char in matched_possible_characters:
    #         char_arr = char[self.parkingLibrary.alignments.C.name].copy()
    #         if alignment in char:
    #             char_arr.extend(char[alignment].copy())
    #         combinations = self.generate_combinations_for_current_characters(combinations, char_arr)
    #     return combinations
    #
    # def generate_combinations_for_current_characters(self, prev_strings, curr_characters):
    #     new_strings = []
    #     for prev_string in prev_strings:
    #         for curr_character in curr_characters:
    #             new_strings.append(prev_string + curr_character)
    #     return new_strings

    def get_levenshtein_distance_map(self, input_string, parking_phrases):
        levenshtein_map = {}
        for parking_phrase in parking_phrases:
            distance = self.find_levenshtein_distance(input_string, parking_phrase)
            levenshtein_map[parking_phrase] = distance
        sorted_levenshtein_map = sorted(levenshtein_map.items(), key=lambda item: item[1])
        return collections.OrderedDict(sorted_levenshtein_map)

    def find_levenshtein_distance(self, str1, str2):
        # str1 => char comb,    str2 => parking vocab
        prev_arr = list(range(0, len(str2) + 1))
        counter = 1
        for i in range(len(str1)):
            curr_arr = list()
            curr_arr.append(counter)
            for j in range(1, len(str2) + 1):
                if str1[i] == str2[j - 1]:
                    curr_arr.append(prev_arr[j - 1])
                else:
                    min_value = min(curr_arr[j - 1], prev_arr[j - 1], prev_arr[j])
                    curr_arr.append(min_value + 1)
            counter += 1
            prev_arr = curr_arr
        return prev_arr[len(str2)]
