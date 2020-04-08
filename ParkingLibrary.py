from enum import Enum


class ParkingLibrary:
    def __init__(self):
        self.alignments = Enum("alignments", ["C", "T", "B", "L", "R"])  # => Center, Top, Bottom, Left, Right

        # ToDo : Create the dictionary for lower case letters as well
        self.possible_characters = {
            "7": {
                self.alignments.C.name: ["7", "T"],
                self.alignments.B.name: ["Z"],
                self.alignments.L.name: ["N"],  # n => 7
            },
            "O": {
                self.alignments.C.name: ["O", "0"],
                self.alignments.T.name: ["6"],
                self.alignments.B.name: ["9"],
            },
            "N": {
                self.alignments.C.name: ["N"],
                self.alignments.R.name: ["M"],
            },
            "F": {
                self.alignments.C.name: ["F"],
                self.alignments.B.name: ["E"],
                self.alignments.R.name: ["A"],
            },
            "1": {
                self.alignments.C.name: ["1", "L", "I"],
                self.alignments.B.name: ["E"],
                self.alignments.R.name: ["P", "N", "R", "M", "B", "D", "E", "F", "H", "K", "W"],
                self.alignments.L.name: ["N", "M", "W"],
                self.alignments.T.name: ["T", "Y"],
            }
        }

        self.parking_vocabulary = [
            "ZONE",
            "ONE"
        ]
