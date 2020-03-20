class BoundingBox:
    def __init__(self, origin_x, origin_y, width, height, text):
        self.origin_x = round(origin_x, 2)
        self.origin_y = round(origin_y, 2)
        self.width = round(width, 2)
        self.height = round(height, 2)
        self.text = text
