import ParkingWordToken
from enum import Enum


class ParkingPhraseTemplates(Enum):

    TIME_WINDOW = [
        [ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name,
         ParkingWordToken.ParkingWordToken.RANGE.name,
         ParkingWordToken.ParkingWordToken.TIME_OF_DAY.name],
    ]

    # WEEK = [
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
