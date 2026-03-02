from enum import IntEnum


class DumperMode(IntEnum):
    """Mode level for dumper."""

    TEST = 0
    DEBUG = 1
    PROD = 2
