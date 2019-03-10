from typing import TypeVar, Type, Mapping, Any

T = TypeVar("T")


def from_dict(data_type: Type[T], mapping: Mapping[str, Any]) -> T:
    return data_type(**mapping)  # type: ignore


__all__ = ["from_dict"]
