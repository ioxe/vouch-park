class TemplateBoundingBox:
    def __init__(self, origin_x, origin_y, width, height, text, is_regex, is_info_imp, is_bounding_box_width_imp):
        self.origin_x = round(origin_x, 2)
        self.origin_y = round(origin_y, 2)
        self.width = round(width, 2)
        self.height = round(height, 2)
        self.text = text
        self.is_regex = is_regex
        self.is_info_imp = is_info_imp
        self.is_bounding_box_width_imp = is_bounding_box_width_imp
