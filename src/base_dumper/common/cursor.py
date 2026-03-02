from abc import (
    ABC,
    abstractmethod,
)
from typing import NoReturn


class AbstractCursor(ABC):
    """Base cursor abstract class.
    This class must have this two methods besides his own."""

    @abstractmethod
    def execute(self, *args, **kwargs) -> NoReturn:
        """Abstract execute method."""

    @abstractmethod
    def close(self, *args, **kwargs) -> NoReturn:
        """Abstract close method."""
