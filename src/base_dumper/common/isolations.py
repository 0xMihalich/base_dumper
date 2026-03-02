from enum import Enum


class IsolationLevel(str, Enum):
    """Transaction isolation level."""

    uncommitted = "READ UNCOMMITTED"
    committed = "READ COMMITTED"
    repeatable = "REPEATABLE READ"
    serializable = "SERIALIZABLE"
