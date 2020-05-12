import SequenceAlignmentService
import InputTransformerService
import ParkingLineCorrectionService
import ParkingTokenizationService


class ParkingSignCorrectionService:

    def __init__(self):
        self.sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
        self.input_transformer_Service = InputTransformerService.InputTransformerService()
        self.parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()
        self.parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()

    def correct_parking_sign(self, inputs):
        merged_sequence = self.sequence_alignment_service.pairwise_align_and_merge_sequences(inputs[0], inputs[1])
        tree_head = self.input_transformer_Service.transform_input(merged_sequence)
        result = str(self.dfs(tree_head, ""))
        print("\n\n Result: " + str(result))
        return None

    def dfs(self, node, prev_lines):
        if len(node.val) > 0:
            node.corrections = self.parking_line_correction_service.get_line_corrections(node.val)
            node.tokens = self.parking_tokenization_service.get_matching_tokens([node.val, node.corrections])
            print(str(node.val) + " : " + str(node.corrections))
            print("\t\t" + str(node.tokens))
            prev_lines += ", " + node.val
        if len(node.children) == 0:
            return [prev_lines.strip(' ,')]

        merged_list = []
        for child in node.children:
            merged_list.extend(self.dfs(child, prev_lines))
        return merged_list
