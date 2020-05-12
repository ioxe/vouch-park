from enum import Enum


class ParkingWordToken(Enum):

    TIME_OF_DAY = [r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*AM\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*PM\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*A\.M\.\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*P\.M\.\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*A\.M\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*AM\.\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*P\.M\b',
                   r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*PM\.\b',
                   r'\bNOON\b',
                   r'\bMID\s*(-)?\s*NIGHT\b']

    DAY_OF_WEEK = [r'\bMON(DAY)?(S)?\b',
                   r'\bTUE(DAY)?(S)?\b',
                   r'\bWED(DAY)?(S)?\b',
                   r'\bTHU(DAY)?(S)?\b',
                   r'\bFRI(DAY)?(S)?\b',
                   r'\bSAT(DAY)?(S)?\b',
                   r'\bSUN(DAY)?(S)?\b']

    WEEK_OF_MONTH = [r'\b1\s*(-)?\s*ST\b',
                     r'\b2\s*(-)?\s*ND\b',
                     r'\b3\s*(-)?\s*RD\b',
                     r'\b4\s*(-)?\s*TH\b',
                     r'\b5\s*(-)?\s*TH\b']

    HOUR_PARKING = [r'\b1{0,1}[0-9]{1}\b',
                    r'\b2{0,1}[0-4]{1}\b']

    MINUTES_PARKING = [r'\b[1-5]{0,1}[0-9]{1}\b',
                       r'\b60\b']

    DATE = [r'\b((0?[1-9])|(1[0-2]))\s*[-\/]\s*((0?[1-9])|([1-2][0-9])|(3[0-1]))\s*[-\/]\s*((19|20)?\d{2})\b']



