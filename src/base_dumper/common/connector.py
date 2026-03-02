from typing import NamedTuple


class DBConnector(NamedTuple):
    """Base connector."""

    host: str
    dbname: str
    user: str
    password: str
    port: int
