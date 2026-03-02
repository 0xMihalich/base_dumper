class BaseDumperError(Exception):
    """Dumper base error."""


class BaseDumperTypeError(BaseDumperError, TypeError):
    """Dumper type error."""


class BaseDumperValueError(BaseDumperError, ValueError):
    """Dumper value error."""
