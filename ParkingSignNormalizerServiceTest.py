import unittest
import ParkingSignNormalizerService
import BoundingBox


class ParkingSignNormalizerServiceTest(unittest.TestCase):
    test_Cases = [
        # test case 1
        [
            [
                BoundingBox.BoundingBox(0.14, 0.84, 0.73, 0.10, "TOW-AWAY"),
                BoundingBox.BoundingBox(0.05, 0.60, 0.87, 0.19, "NO STOPPING"),
                BoundingBox.BoundingBox(0.08, 0.41, 0.83, 0.14, "10AM TO 6PM"),
                BoundingBox.BoundingBox(0.15, 0.30, 0.71, 0.08, "EVERYDAY"),
                BoundingBox.BoundingBox(0.26, 0.19, 0.49, 0.05, "FOR TOWED CARS"),
                BoundingBox.BoundingBox(0.26, 0.11, 0.51, 0.05, "PHONE 123-1234")
            ],
            [
                BoundingBox.BoundingBox(0.10, 0.88, 0.84, 0.12, "TOW-AWAY"),
                BoundingBox.BoundingBox(0.00, 0.59, 1.00, 0.23, "NO STOPPING"),
                BoundingBox.BoundingBox(0.03, 0.36, 0.96, 0.17, "10AM TO 6PM"),
                BoundingBox.BoundingBox(0.11, 0.23, 0.82, 0.10, "EVERYDAY"),
                BoundingBox.BoundingBox(0.24, 0.10, 0.56, 0.06, "FOR TOWED CARS"),
                BoundingBox.BoundingBox(0.24, 0.00, 0.59, 0.06, "PHONE 123-1234")
            ]
        ],
    ]

    def test_parking_sign_normalizer(self):

        parking_Sign_normalizer_service = ParkingSignNormalizerService.ParkingSignNormalizerService()

        for test_case in self.test_Cases:
            actual_bounding_boxes = parking_Sign_normalizer_service.normalize_parking_sign(test_case[0])
            expected_bounding_boxes = test_case[1]
            self.assertEqual(len(expected_bounding_boxes), len(actual_bounding_boxes))
            for i in range(len(expected_bounding_boxes)):
                self.assertEqual(expected_bounding_boxes[i].origin_x, actual_bounding_boxes[i].origin_x)
                self.assertEqual(expected_bounding_boxes[i].origin_y, actual_bounding_boxes[i].origin_y)
                self.assertEqual(expected_bounding_boxes[i].width, actual_bounding_boxes[i].width)
                self.assertEqual(expected_bounding_boxes[i].height, actual_bounding_boxes[i].height)


if __name__ == '__main__':
    unittest.main()
