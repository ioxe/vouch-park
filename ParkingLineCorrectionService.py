import ParkingWordsLibrary
import ParkingWordCorrectionService
import ParkingLineCorrectionDomain


class ParkingLineCorrectionService:

    def __init__(self):
        self.parking_words_library = ParkingWordsLibrary.ParkingWordsLibrary()
        self.parking_word_correction_service = ParkingWordCorrectionService.ParkingWordCorrectionService()

    def get_line_corrections(self, input_line):
        parking_line_correction_domain = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain()
        parking_line_correction_domain.text = input_line

        words = input_line.split()

        if len(words) > 1:
            possible_lines = self.recurse([words[0]], words, 1)
            # print(str(possible_lines))

            # Limiting words by the maximum length in the parking library
            valid_possible_lines = []
            for possible_line in possible_lines:
                is_line_valid = True
                for word in possible_line:
                    if len(word) > self.parking_words_library.max_len_of_parking_words:
                        is_line_valid = False
                if is_line_valid:
                    valid_possible_lines.append(possible_line)

            # Get all possible words corrections
            possible_words_to_score = {}
            possible_words_to_corrections = {}
            possible_results = []
            for valid_possible_line in valid_possible_lines:
                line_score = 0
                for valid_possible_word in valid_possible_line:
                    if valid_possible_word not in possible_words_to_score:
                        current_result = self.parking_word_correction_service.correct_word(valid_possible_word)
                        possible_words_to_corrections[valid_possible_word] = current_result
                        possible_words_to_score[valid_possible_word] = min(current_result.values())  # Minimum Levenshtein distance
                    line_score += possible_words_to_score[valid_possible_word]
                line_score += len(valid_possible_line) - 1  # Add number of empty spaces between the words
                possible_results.append([valid_possible_line, line_score])

            sorted_possible_results = sorted(possible_results, key=lambda x: (x[1], x[0]))

            # Shortlist lines => Get the lines having minimum score
            min_score = sorted_possible_results[0][1]
            shortlisted_possible_results = []
            for sorted_possible_result in sorted_possible_results:
                if sorted_possible_result[1] > min_score:
                    break
                shortlisted_possible_results.append(sorted_possible_result[0])

            for shortlisted_possible_result in shortlisted_possible_results:
                line_combination = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination()
                for word in shortlisted_possible_result:
                    part_of_line = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination.PartOfLine()
                    part_of_line.text = word
                    part_of_line.word_corrections = possible_words_to_corrections[word]
                    line_combination.parts_of_line.append(part_of_line)
                parking_line_correction_domain.line_combinations.append(line_combination)
        else:
            current_result = self.parking_word_correction_service.correct_word(input_line)
            part_of_line = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination.PartOfLine()
            part_of_line.text = input_line
            part_of_line.word_corrections = current_result
            line_combination = ParkingLineCorrectionDomain.ParkingLineCorrectionDomain.LineCombination()
            line_combination.parts_of_line.append(part_of_line)
            parking_line_correction_domain.line_combinations.append(line_combination)

        # return final_result
        return parking_line_correction_domain

    def recurse(self, current, words, index):
        left_val = current.copy()
        left_val.append(words[index])
        right_val = current.copy()
        right_val[len(right_val) - 1] = right_val[len(right_val) - 1] + " " + words[index]
        if index == len(words) - 1:
            return [left_val, right_val]
        left_result = self.recurse(left_val, words, index + 1)
        right_result = self.recurse(right_val, words, index + 1)
        left_result.extend(right_result)
        return left_result
