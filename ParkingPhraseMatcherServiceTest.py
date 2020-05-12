import unittest
import SequenceAlignmentService
import InputTransformerService
import ParkingLineCorrectionService
import ParkingTokenizationService
import ParkingPhraseMatcherService


class ParkingPhraseMatcherServiceTest(unittest.TestCase):
    test_cases = [
        [
            ["HOUR,PARKING,7A.M. TO 6P.,EXCEPT SUNDAYS", "HOUR,PARKING,oP. (A.M.TO,EXCEPT SUNDAYS"],
            []
        ],
    ]
    sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
    input_transformer_Service = InputTransformerService.InputTransformerService()
    parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()
    parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()

    def test(self):

        parking_phrase_matcher_service = ParkingPhraseMatcherService.ParkingPhraseMatcherService()

        for test_case in self.test_cases:
            # Setup
            merged_sequence = self.sequence_alignment_service.pairwise_align_and_merge_sequences(test_case[0][0],
                                                                                                 test_case[0][1])
            tree_head = self.input_transformer_Service.transform_input(merged_sequence)
            self.build_tree(tree_head, "")

            # call ParkingPhraseMatcherService
            parking_phrase_matcher_service.get_parking_phrase_matches(tree_head)

    def build_tree(self, node, prev_lines):
        if len(node.val) > 0:
            node.corrections = self.parking_line_correction_service.get_line_corrections(node.val)
            node.tokens = self.parking_tokenization_service.get_matching_tokens([node.val, node.corrections])
            prev_lines += ", " + node.val
        if len(node.children) == 0:
            return [prev_lines.strip(' ,')]

        merged_list = []
        for child in node.children:
            merged_list.extend(self.build_tree(child, prev_lines))
        return merged_list
