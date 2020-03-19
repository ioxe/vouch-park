class BoundingBox:
    def __init__(self, origin_x, origin_y, width, height, text, is_important):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self.text = text
        self.is_important = is_important
