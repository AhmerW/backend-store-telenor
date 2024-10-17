from typing import Any, Dict, Tuple, Union

PLACEHOLDER = "$"


class Serial(dict):
    def __getitem__(self, k: Any) -> str:
        return f"{PLACEHOLDER}{list(self.keys()).index(k) + 1}"


class Query:
    """
    Allows use to write queries with {placeholder} syntax instead of using $(some number).
    Example:
        select * from table where value = ${value} or value = ${value} and other_value = ${other_value}
        -> select * from table where value = $1 or value = $1 and other_value = $2

    """

    __slots__ = ("_query",)

    def __init__(self, query: str) -> None:
        self._query = query

    def __call__(self, **values):
        return self.format(**values)

    @property
    def query(self) -> str:
        return self._query

    def format(
        self, **values: Dict[str, Any]
    ) -> Union[Tuple[str, Dict[str, Any]], str]:
        if isinstance(self._query, str):
            return self._query.format_map(Serial(**values),), *list(
                values.values(),
            )

        return self._query
