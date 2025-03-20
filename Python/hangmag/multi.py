import enum


class Role(enum.Enum):
    CHOOSER = 1
    GUESSER = 2

class MultiGame:
    def __init__(self, role):
        