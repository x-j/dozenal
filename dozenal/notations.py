from typing import Dict
from copy import deepcopy


class NotationSystem:

    def __init__(self, dec_symbol: str, el_symbol: str):
        self.DEC_SYMBOL = dec_symbol
        self.EL_SYMBOL = el_symbol


pitman = NotationSystem('↊', '↋')
teneleven = NotationSystem("T", "E")
ab = NotationSystem("A", "B")
xz = NotationSystem("X", "Z")
ascii_dwiggins = NotationSystem("X", "E")

DOZENAL_NOTATIONS_DICT: Dict[str, NotationSystem] = {"pitman": pitman, "pt": pitman,
                                                       "ascii": ascii_dwiggins, "dwiggins": ascii_dwiggins,
                                                       "ad": ascii_dwiggins,
                                                       "te": teneleven, "teneleven": teneleven,
                                                       "ab": ab,
                                                       "xz": xz}


def get_notation(key: str) -> NotationSystem:
    return deepcopy((DOZENAL_NOTATIONS_DICT[key]))
