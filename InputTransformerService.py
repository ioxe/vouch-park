import ParkingLineCorrectionService
import SequenceAlignmentService


class InputTransformerService:
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = []

    def __init__(self):
        self.sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
        self.parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()

    def transform_input(self, input_arr):
        head = self.Node("")
        print(head.val)
        self.recurse_to_transform(head, input_arr, -1, "")
        return self.dfs(head, "")

    def recurse_to_transform(self, node, input_arr, current_index, line_so_far):
        #  Base case
        if current_index + 1 >= len(input_arr):
            return

        current_index += 1

        while current_index < len(input_arr) and len(input_arr[current_index]) == 1 and "," != input_arr[current_index][0]:
            line_so_far += input_arr[current_index][0]
            current_index += 1

        if current_index >= len(input_arr):
            child = self.Node(line_so_far)
            node.children.append(child)
            # print(child.val)

        elif len(input_arr[current_index]) > 1:
            for i in range(len(input_arr[current_index])):
                if input_arr[current_index][i] == ",":
                    child = self.Node(line_so_far)
                    node.children.append(child)
                    # print(child.val)
                    self.recurse_to_transform(child, input_arr, current_index, "")
                else:
                    self.recurse_to_transform(node, input_arr, current_index, line_so_far + input_arr[current_index][i])

        elif len(input_arr[current_index]) == 1:
            child = self.Node(line_so_far)
            node.children.append(child)
            # print(child.val)
            self.recurse_to_transform(child, input_arr, current_index, "")

    def dfs(self, node, prev_lines):
        prev_lines += " " + node.val
        if len(node.children) == 0:
            return [prev_lines.strip()]

        merged_list = []
        for child in node.children:
            merged_list.extend(self.dfs(child, prev_lines))
        return merged_list
