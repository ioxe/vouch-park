import ParkingLineCorrectionService
import SequenceAlignmentService
import Node


class InputTransformerService:

    def __init__(self):
        self.sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
        self.parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()

    def transform_input(self, input_arr):
        head = Node.Node("")
        print(head.val)
        self.recurse_to_transform(head, input_arr, -1, "")
        return head

    def recurse_to_transform(self, node, input_arr, current_index, line_so_far):
        #  Base case
        if current_index + 1 >= len(input_arr):
            return

        current_index += 1

        while current_index < len(input_arr) and len(input_arr[current_index]) == 1 and "," != input_arr[current_index][0]:
            line_so_far += input_arr[current_index][0]
            current_index += 1

        if current_index >= len(input_arr):
            child = Node.Node(line_so_far)
            node.children.append(child)
            # print(child.val)

        elif len(input_arr[current_index]) > 1:
            for i in range(len(input_arr[current_index])):
                if input_arr[current_index][i] == ",":
                    child = Node.Node(line_so_far)
                    node.children.append(child)
                    # print(child.val)
                    self.recurse_to_transform(child, input_arr, current_index, "")
                else:
                    self.recurse_to_transform(node, input_arr, current_index, line_so_far + input_arr[current_index][i])

        elif len(input_arr[current_index]) == 1:
            child = Node.Node(line_so_far)
            node.children.append(child)
            # print(child.val)
            self.recurse_to_transform(child, input_arr, current_index, "")