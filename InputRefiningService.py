class InputRefiningService:
    def refine_input(self, input_arr):
        returned_arr = self.combine_phrases(input_arr)
        return returned_arr

    def combine_phrases(self, input_arr):
        returned_arr = []
        index_input_arr = 0
        is_Except_found = False
        while index_input_arr < len(input_arr):
            sanitized_text = str(input_arr[index_input_arr]).strip().upper()

            # cases for "TO"
            if sanitized_text == "TO" and index_input_arr > 0:  # Examples - "[Pay] [To] [Park]" and "[9AM] [TO] [5PM]"
                index_input_arr += 1
                returned_arr[len(returned_arr) - 1] += " TO " + input_arr[index_input_arr]

            elif sanitized_text.startswith("TO") and index_input_arr > 0:  # Examples - "[Pay] [To Park]"
                returned_arr[len(returned_arr) - 1] += " " + input_arr[index_input_arr]

            elif sanitized_text.endswith("TO") and index_input_arr + 1 < len(input_arr):  # Examples - "[Pay To] [Park]"
                returned_arr.append(input_arr[index_input_arr] + " " + input_arr[index_input_arr + 1])
                index_input_arr += 1

            # cases for "PARKING"
            elif sanitized_text == "PARKING" and index_input_arr > 0:  # Examples - "[2 HOUR] [PARKING]" and "[NO] [PARKING]"
                returned_arr[len(returned_arr) - 1] += " PARKING"

            # cases for "EXCEPT"
            elif is_Except_found is True:
                returned_arr.append("EXCEPT " + input_arr[index_input_arr])

            elif sanitized_text.find("EXCEPT") > -1:
                returned_arr.append(input_arr[index_input_arr])
                is_Except_found = True

            # default case
            else:
                returned_arr.append(input_arr[index_input_arr])

            index_input_arr += 1
        return returned_arr

    def correct_words(self, input_arr):
        pass
