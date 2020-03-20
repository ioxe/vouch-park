import BoundingBox


class ParkingSignNormalizerService:
    def normalize_parking_sign(self, bounding_boxes):
        min_x = 1
        min_y = 1
        max_x = 0
        max_y = 0

        # find the parking sign bounding box
        for box in bounding_boxes:
            min_x = min(min_x, box.origin_x)
            min_y = min(min_y, box.origin_y)
            max_x = max(max_x, box.origin_x + box.width)
            max_y = max(max_y, box.origin_y + box.height)

        print("Min_x:" + str(min_x) + ", Min_y:" + str(min_y) + ", max_x:" + str(max_x) + ", max_y:" + str(max_y))
        # set parking sign measurements
        parking_sign_width = max_x - min_x
        parking_sign_height = max_y - min_y

        print("parking_sign_width:" + str(parking_sign_width) + ", parking_sign_height:" + str(parking_sign_height))

        # change the input bounding boxes relative to the parking sign
        output_bounding_boxes = []
        for box in bounding_boxes:
            origin_x = round((box.origin_x - min_x) / parking_sign_width, 2)
            origin_y = round((box.origin_y - min_y) / parking_sign_height, 2)
            width = round(((box.origin_x + box.width - min_x) / parking_sign_width) - origin_x, 2)
            height = round(((box.origin_y + box.height - min_y) / parking_sign_height) - origin_y, 2)
            output_bounding_box = BoundingBox.BoundingBox(origin_x, origin_y, width, height, box.text)
            output_bounding_boxes.append(output_bounding_box)

        return output_bounding_boxes
