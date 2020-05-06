from enum import Enum


class ParkingWordToken(Enum):
    TIME_OF_DAY = [r'\b[0-1]{0,1}[0-9]{1}\s*[\.:]?\s*\d{0,2}\s*[AP]\.?[M]\.?\b',
                   r'\bNOON\b',
                   r'\bMID\s*(-)?\s*NIGHT\b']

    DAY_OF_WEEK = [r'\bMON(DAY)?\b',
                   r'\bTUE(DAY)?\b',
                   r'\bWED(DAY)?\b',
                   r'\bTHU(DAY)?\b',
                   r'\bFRI(DAY)?\b',
                   r'\bSAT(DAY)?\b',
                   r'\bSUN(DAY)?\b']

    WEEK_OF_MONTH = [r'\b1\s*(-)?\s*ST\b',
                     r'\b2\s*(-)?\s*ND\b',
                     r'\b3\s*(-)?\s*RD\b',
                     r'\b4\s*(-)?\s*TH\b',
                     r'\b5\s*(-)?\s*TH\b']

    HOUR_PARKING = [r'\b1{0,1}[0-9]{1}\b',
                    r'\b2{0,1}[0-4]{1}\b']

    MINUTES_PARKING = [r'\b[1-5]{0,1}[0-9]{1}\b',
                       r'\b6{0,1}0{1}\b']

