import ParkingWordToken
from enum import Enum


class ParkingPhraseTemplates(Enum):
    def __init__(self):

        self.time_Window = [
            [r"^\s*" + ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name,
             r'([\.-])?\s*([\.-])?\s*',
             ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name + r"\s*$"],

            [r"^\s*" + ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name,
             r'([\.-])?\s*TO\s*',
             ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name + r"\s*$"],
        ]

        # self.week_of_month = [
        #     [r"^\s*" + ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name + r"\s*$"],
        #
        #     [r"^\s*" + ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*TO\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name + r"\s*$"],
        #
        #     [r"^\s*" + ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name + r"\s*$"],
        #
        #     [r"^\s*" + ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name + r"\s*$"],
        #
        #     [r"^\s*" + ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name,
        #      r'\s*([\.-,])?\s*(AND|&)?\s*([\.-,])?\s*',
        #      ParkingWordToken.ParkingWordToken.WEEK_OF_MONTH.name + r"\s*$"],
        # ]
