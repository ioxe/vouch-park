import Node
import math


class Dictionary:

    def __init__(self):
        self.root_node = Node.Node("")
        self.build_parking_dictionary()
        self.error_threshold_percent = 30

    def find_close_phrases(self, input_phrase):
        error_suggestion_probability = math.ceil(len(input_phrase) * self.error_threshold_percent / 100)

    def dfs_closeness(self, node, phrase_so_far, error_num, close_phrases):
        pass
        # phrase_so_far += node.val
        # if(error_num)
        # for each_node in node.next_nodes:
        #     self.dfs_closeness(each_node, phrase_so_far)
        # if node.is_end_of_phrase:
        #     print(phrase_so_far)
        #     return

    def build_parking_dictionary(self):
        self.add_phrase("NO PARKING")
        self.add_phrase("NO STOPPING")
        self.add_phrase("TOW AWAY")
        self.add_phrase("PAY TO PARK")
        self.add_phrase("HOUR PARKING")
        self.add_phrase("EXCEPT")
        self.add_phrase("MONDAY TO FRIDAY")
        self.add_phrase("MON TO FRI")
        self.add_phrase("MONDAY THRU FRIDAY")
        self.add_phrase("MON THRU FRI")
        self.add_phrase("EXCEPT")
        self.add_phrase("EXCEPT SUNDAYS")
        self.add_phrase("EXCEPT HOLIDAYS")
        self.add_phrase("OF THE MONTH")

    def add_phrase(self, phrase):
        sanitized_phrase = phrase.strip().upper()
        length = len(sanitized_phrase)
        current_node = self.root_node
        if length > 0:
            i = 0
            while i < length:
                is_current_node_already_exist = False
                for node in current_node.next_nodes:
                    if sanitized_phrase[i] == node.val:
                        is_current_node_already_exist = True
                        current_node = node

                if not is_current_node_already_exist:
                    # This ignores the recurring white spaces between the words in a phrase
                    if sanitized_phrase[i] == " ":
                        while sanitized_phrase[i + 1] == " ":
                            i += 1
                    new_node = Node.Node(sanitized_phrase[i])
                    current_node.next_nodes.append(new_node)
                    current_node = new_node
                i += 1
            current_node.is_end_of_phrase = True

    def print_dictionary(self):
        self.dfs_print(self.root_node, "")

    def dfs_print(self, node, phrase_so_far):
        phrase_so_far += node.val
        for each_node in node.next_nodes:
            self.dfs_print(each_node, phrase_so_far)
        if node.is_end_of_phrase:
            print(phrase_so_far)
            return


dictionary = Dictionary()
dictionary.find_close_phrases("Hello sunshine")
dictionary.print_dictionary()
