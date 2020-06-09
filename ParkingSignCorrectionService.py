import SequenceAlignmentService
import GraphBuilderService
import ParkingLineCorrectionService
import ParkingTokenizationService


class ParkingSignCorrectionService:

    def __init__(self):
        self.sequence_alignment_service = SequenceAlignmentService.SequenceAlignmentService()
        self.graph_builder_Service = GraphBuilderService.GraphBuilderService()
        self.parking_line_correction_service = ParkingLineCorrectionService.ParkingLineCorrectionService()
        self.parking_tokenization_service = ParkingTokenizationService.ParkingTokenizationService()

    def correct_parking_sign(self, inputs):
        aligned_sequence = self.sequence_alignment_service.pairwise_align_and_merge_sequences(inputs[0], inputs[1])
        vertices, edges = self.graph_builder_Service.transform_array_to_graph(aligned_sequence)

        # Get line corrected vertices
        line_corrected_vertices = {}
        for vertex_id, text in vertices.items():
            line_corrected_vertices[vertex_id] = self.parking_line_correction_service.get_line_corrections(text)

        # Get tokenized vertices
        tokenized_vertices = {}
        for vertex_id, line_corrected_vertex in line_corrected_vertices.items():
            tokenized_vertices[vertex_id] = self.parking_tokenization_service.get_matching_tokens(line_corrected_vertex)
            print(str(vertex_id) + " : " + str(tokenized_vertices[vertex_id]))

        # TODO : Add Phrase Matcher
        return []


