from enum import Enum


class ParkingLibrary:
    def __init__(self):
        self.alignments = Enum("alignments", ["C", "T", "B", "L", "R"])  # => Center, Top, Bottom, Left, Right

        # ToDo : Create the dictionary for lower case letters as well
        self.possible_characters = {
            "A": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "B": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "C": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "D": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "E": {
                self.alignments.C.name: ["E"],
                self.alignments.R.name: ["B"]
            },
            "F": {
                self.alignments.C.name: ["F"],
                self.alignments.B.name: ["E"],
                self.alignments.R.name: ["A"],
            },
            "G": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "H": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "I": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "J": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "K": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "L": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "M": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "N": {
                self.alignments.C.name: ["N"],
                self.alignments.R.name: ["M"],
            },
            "O": {
                self.alignments.C.name: ["O", "0"],
                self.alignments.T.name: ["6"],
                self.alignments.B.name: ["9"],
            },
            "P": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "Q": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "R": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "S": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "T": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "U": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "V": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "W": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "X": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "Y": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "Z": {
                self.alignments.C.name: ["Z"]
            },
            "0": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "1": {
                self.alignments.C.name: ["1", "L", "I"],
                self.alignments.B.name: ["E"],
                self.alignments.R.name: ["P", "N", "R", "M", "B", "D", "E", "F", "H", "K", "W"],
                self.alignments.L.name: ["N", "M", "W"],
                self.alignments.T.name: ["T", "Y"],
            },
            "2": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "3": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "4": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "5": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "6": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "7": {
                self.alignments.C.name: ["7", "T"],
                self.alignments.B.name: ["Z"],
                self.alignments.L.name: ["N"],  # n => 7
            },
            "8": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },
            "9": {
                self.alignments.C.name: [],
                self.alignments.B.name: [],
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: [],
            },


        }

        self.parking_vocabulary = [
            "ZONE",
            "ONE"
        ]
