from enum import Enum


class ParkingLibrary:
    def __init__(self):

        self.alignments = Enum("alignments", ["C", "T", "B", "L", "R"])  # => Center, Top, Bottom, Left, Right

        # ToDo : Create the dictionary for lower case letters as well
        self.possible_characters = {
            "A": {
                self.alignments.C.name: ["A"],
                self.alignments.B.name: ["8", "B"],  # 8, B
            },
            "a": {
                self.alignments.C.name: ["A"],  # a
                self.alignments.B.name: ["9", "Q", "G"],  # 9, q, g
                self.alignments.T.name: ["D"],  # d
            },
            "B": {
                self.alignments.C.name: ["B", "H", "8"],
            },
            "b": {
                self.alignments.C.name: ["B"],  # b
                self.alignments.B.name: ["P", "R"],  # p, R
            },
            "C": {
                self.alignments.C.name: ["C", "O", "0"],
                self.alignments.R.name: ["O", "0", "Q", "D", "A"],  # o, 0 , q, d, a
            },
            "c": {
                self.alignments.C.name: ["C", "O", "0"],
                self.alignments.R.name: ["O", "0", "Q", "D", "A"],  # o, 0 , q, d, a
            },
            "D": {
                self.alignments.C.name: ["D", "O", "0"],
                self.alignments.B.name: ["P", "R", "A", "8"],
                self.alignments.T.name: ["8"],
            },
            "d": {
                self.alignments.C.name: ["D", "A"],  # d, a
                self.alignments.B.name: ["9", "Q", "G"],  # 9, q, g
            },
            "E": {
                self.alignments.C.name: ["E"],
                self.alignments.R.name: ["B", "8"]
            },
            "e": {
                self.alignments.C.name: ["E", "C"],
            },
            "F": {
                self.alignments.C.name: ["F"],
                self.alignments.B.name: ["E"],
                self.alignments.R.name: ["A"],
            },
            "f": {
                self.alignments.C.name: ["F"],
            },
            "G": {
                self.alignments.C.name: ["G", "C"],
                self.alignments.R.name: ["O", "0", "Q"],  # O, 0, Q
            },
            "g": {
                self.alignments.C.name: ["G", "9"],  # g, 9
                self.alignments.B.name: ["Q"],  # q
                self.alignments.R.name: [],
                self.alignments.L.name: [],
                self.alignments.T.name: ["A"],
            },
            "H": {
                self.alignments.C.name: ["H"],
                self.alignments.T.name: ["A"],
            },
            "h": {
                self.alignments.C.name: ["H"],
                self.alignments.B.name: ["B"],  # b
            },
            "I": {
                self.alignments.C.name: ["I", "1", "L"],  # I, 1, l
                self.alignments.B.name: ["J"],
                self.alignments.R.name: ["P", "N", "R", "M", "B", "D", "E", "F", "H", "K", "W"],
                self.alignments.L.name: ["N", "M", "W"],
                self.alignments.T.name: ["T", "Y"],
            },
            "i": {
                self.alignments.C.name: ["I", "1", "L"],  # I, 1, l
                self.alignments.B.name: ["J"],  # j
            },
            "J": {
                self.alignments.C.name: ["J"],
                self.alignments.L.name: ["U"],
                self.alignments.T.name: ["9"],
            },
            "j": {
                self.alignments.C.name: ["J"],
            },
            "K": {
                self.alignments.C.name: ["K"],
                self.alignments.T.name: ["R"],
            },
            "k": {
                self.alignments.C.name: ["K"],
                self.alignments.T.name: ["R"],
            },
            "L": {
                self.alignments.C.name: ["L", "I", "1", "T"],  # L, I, 1, t
            },
            "l": {
                self.alignments.C.name: ["L", "I", "1"],  # "L", "I", "1"
                self.alignments.B.name: ["J"],
                self.alignments.R.name: ["P", "N", "R", "M", "B", "D", "E", "F", "H", "K", "W"],
                self.alignments.L.name: ["N", "M", "W"],
                self.alignments.T.name: ["T", "Y"],
            },
            "M": {
                self.alignments.C.name: ["M"],
            },
            "m": {
                self.alignments.C.name: ["M"],
            },
            "N": {
                self.alignments.C.name: ["N"],
                self.alignments.R.name: ["M"],
            },
            "n": {
                self.alignments.C.name: ["N"],  # n
                self.alignments.R.name: ["M"],  # m
            },
            "O": {
                self.alignments.C.name: ["O", "0", "D"],
                self.alignments.T.name: ["6", "D", "A", "B", "8"],  # 6, d, a, b, 8
                self.alignments.B.name: ["9", "p", "G", "Q", "8"],  # 9, p, g, q, 8
            },
            "o": {
                self.alignments.C.name: ["O", "0", "D"],
                self.alignments.T.name: ["6", "D", "A", "B", "8"],  # 6, d, a, b, 8
                self.alignments.B.name: ["9", "p", "G", "Q", "8"],  # 9, p, g, q, 8
            },
            "P": {
                self.alignments.C.name: ["P"],
                self.alignments.B.name: ["R"],
                self.alignments.R.name: ["R"],
            },
            "p": {
                self.alignments.C.name: ["P"],
                self.alignments.B.name: ["R"],
                self.alignments.R.name: ["R"],
            },
            "Q": {
                self.alignments.C.name: ["Q", "O", "0"],
                self.alignments.B.name: ["R"],
            },
            "q": {
                self.alignments.C.name: ["Q"],
                self.alignments.B.name: ["G", "9"],  # g, 9
            },
            "R": {
                self.alignments.C.name: ["R"],
                self.alignments.B.name: ["B", "8"],
            },
            "r": {
                self.alignments.C.name: ["R"],
                self.alignments.B.name: [],
                self.alignments.R.name: ["N", "M", "H"],  # n, m, h
            },
            "S": {
                self.alignments.C.name: ["S", "8", "B"],
            },
            "s": {
                self.alignments.C.name: ["S", "8", "B"],
            },
            "T": {
                self.alignments.C.name: ["T"],
                self.alignments.B.name: ["J", "I", "1"],
            },
            "t": {
                self.alignments.C.name: ["T", "L"],
                self.alignments.R.name: ["U"],
            },
            "U": {
                self.alignments.C.name: ["U", "V"],
                self.alignments.B.name: ["Y"],
                self.alignments.R.name: ["W"],
                self.alignments.L.name: ["W"],
                self.alignments.T.name: ["O", "0"],
            },
            "u": {
                self.alignments.C.name: ["U", "V"],
                self.alignments.B.name: ["Y"],
                self.alignments.R.name: ["W"],
                self.alignments.L.name: ["W"],
                self.alignments.T.name: ["O", "0", "A", "D"],  # o, 0, a, d
            },
            "V": {
                self.alignments.C.name: ["V"],
                self.alignments.B.name: ["Y"],
                self.alignments.R.name: ["W"],
                self.alignments.L.name: ["W"],
            },
            "v": {
                self.alignments.C.name: ["V"],
                self.alignments.B.name: ["Y"],
                self.alignments.R.name: ["W"],
                self.alignments.L.name: ["W"],
            },
            "W": {
                self.alignments.C.name: ["W"],
            },
            "w": {
                self.alignments.C.name: ["W"],
            },
            "X": {
                self.alignments.C.name: ["X"],
            },
            "x": {
                self.alignments.C.name: ["X"],
            },
            "Y": {
                self.alignments.C.name: ["Y"],
            },
            "y": {
                self.alignments.C.name: ["Y"],
            },
            "Z": {
                self.alignments.C.name: ["Z"]
            },
            "z": {
                self.alignments.C.name: ["Z"]
            },
            "0": {
                self.alignments.C.name: ["O", "0", "D"],
                self.alignments.T.name: ["6", "D", "A", "B", "8"],  # 6, d, a, b, 8
                self.alignments.B.name: ["9", "p", "G", "Q", "8"],  # 9, p, g, q, 8
            },
            "1": {
                self.alignments.C.name: ["1", "L", "I"],
                self.alignments.B.name: ["J"],
                self.alignments.R.name: ["P", "N", "R", "M", "B", "D", "E", "F", "H", "K", "W"],
                self.alignments.L.name: ["N", "M", "W"],
                self.alignments.T.name: ["T", "Y"],
            },
            "2": {
                self.alignments.C.name: ["2"],
            },
            "3": {
                self.alignments.C.name: ["3"],
                self.alignments.L.name: ["B"],
            },
            "4": {
                self.alignments.C.name: ["4"],
            },
            "5": {
                self.alignments.C.name: ["5"],
            },
            "6": {
                self.alignments.C.name: ["6", "B"],  # 6, b
            },
            "7": {
                self.alignments.C.name: ["7"],
                self.alignments.B.name: ["Z"],
            },
            "8": {
                self.alignments.C.name: ["8", "B"],
            },
            "9": {
                self.alignments.C.name: ["9", "G"],  # 9, g
            },
            ":": {
                self.alignments.C.name: [":"],
            },
            ".": {
                self.alignments.C.name: ["."],
            },
            "(": {
                self.alignments.C.name: ["("],
                self.alignments.T.name: ["7"],
            },
            "/": {
                self.alignments.C.name: ["/"],
                self.alignments.T.name: ["7"],
            },
            ")": {
                self.alignments.C.name: [")"],
                self.alignments.L.name: ["0"],
            },
            " ": {
                self.alignments.C.name: [" "],
            },
        }

        self.parking_vocabulary = [
            "1",
            "1ST",
            "1AM",
            "1A.M.",
            "1PM",
            "1P.M.",
            "1:30AM",
            "1:30A.M.",
            "1:30PM",
            "1:30P.M.",
            "2",
            "2ND",
            "2AM",
            "2A.M.",
            "2PM",
            "2P.M.",
            "2:30AM",
            "2:30A.M.",
            "2:30PM",
            "2:30P.M.",
            "3",
            "3RD",
            "3AM",
            "3A.M.",
            "3PM",
            "3P.M.",
            "3:30AM",
            "3:30A.M.",
            "3:30PM",
            "3:30P.M.",
            "4",
            "4TH",
            "4AM",
            "4A.M.",
            "4PM",
            "4P.M.",
            "4:30AM",
            "4:30A.M.",
            "4:30PM",
            "4:30P.M.",
            "5",
            "5TH",
            "5AM",
            "5A.M.",
            "5PM",
            "5P.M.",
            "5:30AM",
            "5:30A.M.",
            "5:30PM",
            "5:30P.M.",
            "6",
            "6AM",
            "6A.M.",
            "6PM",
            "6P.M.",
            "6:30AM",
            "6:30A.M.",
            "6:30PM",
            "6:30P.M.",
            "7",
            "7AM",
            "7A.M.",
            "7PM",
            "7P.M.",
            "7:30AM",
            "7:30A.M.",
            "7:30PM",
            "7:30P.M.",
            "8",
            "8AM",
            "8A.M.",
            "8PM",
            "8P.M.",
            "8:30AM",
            "8:30A.M.",
            "8:30PM",
            "8:30P.M.",
            "9",
            "9AM",
            "9A.M.",
            "9PM",
            "9P.M.",
            "9:30AM",
            "9:30A.M.",
            "9:30PM",
            "9:30P.M.",
            "10",
            "10AM",
            "10A.M.",
            "10PM",
            "10P.M.",
            "10:30AM",
            "10:30A.M.",
            "10:30PM",
            "10:30P.M.",
            "11",
            "11AM",
            "11A.M.",
            "11PM",
            "11P.M.",
            "11:30AM",
            "11:30A.M.",
            "11:30PM",
            "11:30P.M.",
            "12",
            "12AM",
            "12A.M.",
            "12PM",
            "12P.M.",
            "12:30AM",
            "12:30A.M.",
            "12:30PM",
            "12:30P.M.",
            "15",
            "20",
            "30",
            "40",
            "45",
            "90",
            "AND",
            "ANY",
            "AREA",
            "AWAY",
            "BLOCK",
            "CLEANING",
            "COMMERCIAL",
            "EVERYDAY",
            "EXCEPT",
            "FEDERAL",
            "FOR",
            "FRI",
            "FRIDAY",
            "HOLIDAY",
            "HOLIDAYS",
            "HOUR",
            "HOURS",
            "MINUTE",
            "MINUTES",
            "MON",
            "MONDAY",
            "MONTH",
            "NO",
            "NOTICE",
            "OF",
            "ONE",
            "ONLY",
            "PARK",
            "PARKING",
            "PAY",
            "PERMIT",
            "PERMITS",
            "REQUIRED",
            "SAT",
            "SATURDAY",
            "STREET",
            "STOPPING",
            "SUN",
            "SUNDAY",
            "SUNDAYS",
            "TIME",
            "TO",
            "TOW",
            "TOWED",
            "TUE",
            "TUESDAY",
            "THE",
            "THU",
            "THURSDAY",
            "THROUGH",
            "THRU",
            "VEHICLE",
            "VEHICLES",
            "WAY",
            "WED",
            "WEDNESDAY",
            "ZONE",
        ]

        self.max_len_of_parking_words = len(max(self.parking_vocabulary, key=len))
