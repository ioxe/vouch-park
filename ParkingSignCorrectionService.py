import SequenceAlignmentService
import InputTransformerService
import ParkingLineCorrectionService
import ParkingTokenizationService


class ParkingSignCorrectionService:

    class WordCorrection:
        def __init__(self):
            self.word = ""
            self.token = []
            self.levenshtein_distance = 0

    class LineCorrection:
        def __init__(self):
            self.part_of_line = ""
            self.token = []
            self.tokened_corrections = []

    class GraphNode:
        def __init__(self):
            self.raw_text = ""
            self.token = []
            self.tokened_corrections = []  # list of line combinations

    def __init__(self):
        self.sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
        self.input_transformer_Service = InputTransformerService.InputTransformerService()
        self.parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()
        self.parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()

    def correct_parking_sign(self, inputs):
        merged_sequence = self.sequence_alignment_service.pairwise_align_and_merge_sequences(inputs[0], inputs[1])
        input_vertices, edges = self.input_transformer_Service.transform_array_to_graph(merged_sequence)

        correction_vertices = {}
        for key, val in input_vertices.items():
            line_corrections = [val, self.parking_line_correction_service.get_line_corrections(val)]
            token_corrections = self.parking_tokenization_service.get_matching_tokens(line_corrections)
            graph_node = self.GraphNode()

            graph_node.raw_text = token_corrections[0]
            graph_node.token = token_corrections[1]
            graph_node.tokened_corrections = token_corrections[2]  # delete later

            for line_combination in token_corrections[2]:
                for line in line_combination:
                    line_correction = self.LineCorrection()
                    line_correction.part_of_line = line[0]
                    line_correction.token = line[1]
                    line_correction.tokened_corrections = line[2]  # delete later

                    # word_corrections = []
                    for part_of_line in line[2]:
                        word_correction = self.WordCorrection()
                        word_correction.word = part_of_line[0]
                        word_correction.token = part_of_line[1]
                        word_correction.levenshtein_distance = part_of_line[2]
                        # word_corrections.append(word_correction)

            correction_vertices[key] = graph_node

        print("\n\n Result: " + str(correction_vertices))
        return None
