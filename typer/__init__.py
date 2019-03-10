from typing import TypeVar, Type, Mapping, Any, get_type_hints, List, Dict

T = TypeVar("T")


class Error:
    pass


class MissingField(Error):
    def __init__(self, field_name: str):
        self.field_name = field_name

    def __str__(self) -> str:
        return f"Missing field '{self.field_name}'"


class WrongType(Error):
    def __init__(self, *, field: str, expected_type: Type, actual_type: Type):
        self.field = field
        self.expected_type = expected_type
        self.actual_type = actual_type

    def __str__(self) -> str:
        return f"""Wrong type for field {self.field}.
        "Expected {self.expected_type} and got {self.actual_type}"""


class TypificationError(Exception):
    def __init__(self, errors: List[Error]):
        string_errors = "\n".join(f"- {e}" for e in errors)
        super().__init__(f"One or more typification errors:\n{string_errors}")


class MissingAnnotations(Exception):
    def __init__(self, data_type: Type[T]):
        super().__init__(f"No type annotations for type {data_type!r}")
        self.data_type = data_type


def from_dict(data_type: Type[T], mapping: Mapping[str, Any]) -> T:
    annotations = get_type_hints(data_type)
    errors: List[Error] = []

    if not annotations:
        raise MissingAnnotations(data_type)

    kwargs: Dict[str, Any] = {}
    for name, expected_type in annotations.items():
        if name not in mapping:
            errors.append(MissingField(name))
            continue

        value = mapping[name]
        if not isinstance(value, expected_type):
            errors.append(
                WrongType(
                    field=name, expected_type=expected_type, actual_type=type(value)
                )
            )
            continue

        kwargs[name] = mapping[name]

    if errors:
        raise TypificationError(errors)

    return data_type(**kwargs)  # type: ignore


__all__ = ["MissingAnnotations", "from_dict"]
