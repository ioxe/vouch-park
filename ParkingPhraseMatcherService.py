import ParkingPhraseTemplates


class ParkingPhraseMatcherService:

    def get_parking_phrase_matches(self, head):
        possible_signs = self.dfs(head, [])
        # print(possible_signs)

        for sign in possible_signs:
            print("*******SIGN*******")
            for line in sign:
                print("Raw i/p: " + str(line[0]))
                print("\tToken: " + str(line[1]))
                print("\t\tCorrections: " + str(line[2]))
                # if len(line[1][1]) == 0:

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
