import Templates
import ParkingSignNormalizerService


class TemplateMatcherService:
    def __init__(self):
        self.error = 0.1

    # def search_template(self, bounding_boxes):
    #
    #     matched_templates = []
    #
    #     # Normalize Parking sign
    #     normalized_bounding_boxes = ParkingSignNormalizerService.ParkingSignNormalizerService().normalize_parking_sign(
    #         bounding_boxes)
    #
    #     for template in Templates.Templates.templates:
    #         if len(template) == len(normalized_bounding_boxes):
    #
    #             for i in range(len(template)):
    #
    #                 if (template[i].is_bounding_box_x_coords_imp and
    #                         template[i].origin_x - self.error <= normalized_bounding_boxes[i].origin_x <= template[i].origin_x - self.error):
    #                     pass
    #
    #     return matched_templates
