import copy


class ParkingTreeFlatteningService:

    def flatten_tree(self, head):
        result = self.dfs(head, [])
        return result

    def dfs(self, node, prev_result):
        current_result = []
        if len(node.val) > 0:
            if len(node.tokens[1]) != 0:
                current_result.extend(self.add_word_to_previous_paths_parent(prev_result, node.tokens[0],
                                                                             node.tokens[1], 0))
            for possible_line in node.tokens[2]:
                t = []
                for part_of_possible_line in possible_line:
                    if len(part_of_possible_line[1]) != 0:
                        current_result.extend(self.add_word_to_previous_paths_parent(prev_result,
                                                                                     part_of_possible_line[0],
                                                                                     part_of_possible_line[1], 0))

                    for correction in part_of_possible_line[2]:
                        current_result.extend(
                            self.add_word_to_previous_paths_child(prev_result, correction[0], correction[1],
                                                                  correction[2]))

        if len(node.children) == 0:
            return current_result

        merged_list = []
        for child in node.children:
            merged_list.extend(self.dfs(child, copy.deepcopy(current_result)))
        return merged_list

    # # Do not call this method if the list of tokens is empty
    def add_word_to_previous_paths_parent(self, prev_list, word, tokens, levenshtein_distance):
        result = []
        for token in tokens:
            results_for_token = copy.deepcopy(prev_list)
            if len(results_for_token) == 0:
                results_for_token = [[word, [token[0]], levenshtein_distance, token[1]]]
            else:
                for result_for_token in results_for_token:
                    result_for_token[0] = result_for_token[0] + " " + word
                    result_for_token[1].append(token[0])
                    result_for_token[2] = result_for_token[2] + levenshtein_distance
                    result_for_token[3] = result_for_token[3] + token[1]
            result.extend(results_for_token)
        return result

    def add_word_to_previous_paths_child(self, prev_list, word, tokens, levenshtein_distance):
        if len(tokens) == 0:
            temp_results = copy.deepcopy(prev_list)
            if len(temp_results) == 0:
                return [[word, [], levenshtein_distance, 0]]
            else:
                for temp_result in temp_results:
                    temp_result[0] = temp_result[0] + " " + word
                    temp_result[2] = temp_result[2] + levenshtein_distance
            return temp_results
        else:
            return self.add_word_to_previous_paths_parent(prev_list, word, tokens, levenshtein_distance)