# tic_tac_toe/logic/models.py

import enum

class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"
