import ParkingPhraseTemplates


class ParkingPhraseMatcherService:

    def get_parking_phrase_matches(self, head):

        # List of nodes
        possible_signs = self.dfs(head, [])
        # print(possible_signs)

        for sign in possible_signs:
            print("*******SIGN*******")
            for line in sign:
                print("Raw i/p: " + str(line[0]) + " ===> Token: " + str(line[1]))
                line_corrections = line[2]
                # print("\t\tLine Corrections: " + str(line_corrections))
                for possible_line in line_corrections:
                    print("\tPossible Line: " + str(possible_line[0][0]) + " ===> Token: " + str(possible_line[0][1]))
                    for part_of_line in possible_line:
                        print("\t\t Part of line: " + str(part_of_line[0]) + " ===> Token: " + str(part_of_line[1]))
                        for correction in part_of_line[2]:
                            print("\t\t\t Correction: " + str(correction[0]) + " ===> Token: " + str(correction[1]) + " ===> Distance: " + str(correction[2]))

    def dfs(self, node, prev_list):
        if len(node.val) > 0:
            prev_list.append(node.tokens)
            # prev_list.append([node.val, node.tokens])

        if len(node.children) == 0:
            return [prev_list]

        merged_list = []
        for child in node.children:
            merged_list.extend(self.dfs(child, prev_list.copy()))
        return merged_list
