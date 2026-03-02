from re import split

from sqlparse import format as sql_format


PATTERN = r";(?=(?:[^']*'[^']*')*[^']*$)"


def __query_formatter(query: str) -> str:
    """Reformat query."""

    return sql_format(sql=query, strip_comments=True).strip().strip(";")


def chunk_query(query: str | None) -> tuple[list[str]]:
    """Chunk multiquery to queryes."""

    if not query:
        return [], []

    parts = [
        part.strip(";").strip()
        for part in split(PATTERN, __query_formatter(query))
        if part.strip(";").strip()
    ]

    if not parts:
        return [], []

    first_part: list[str] = []
    second_part: list[str] = []

    for i, part in enumerate(parts):
        first_part.append(part)

        if (i + 1 < len(parts) and parts[i + 1].lower().startswith(
                ("with", "select")
            )
        ):
            second_part = parts[i + 1:]
            break

    return first_part, second_part
