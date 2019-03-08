from typing import TypeVar, Type, Mapping, Any

T = TypeVar('T')


def from_dict(cls: Type[T]) -> Type[T]:
    def from_dict(mapping: Mapping[str, Any]) -> T:
        return cls(**mapping)  # type: ignore

    setattr(cls, "from_dict", from_dict)
    return cls
