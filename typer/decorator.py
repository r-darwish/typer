from typing import TypeVar, Type, Mapping

T = TypeVar('T')


def from_dict(cls: Type[T]) -> Type[T]:
    def from_dict(mapping: Mapping[str, any]) -> T:
        return cls(**mapping)

    setattr(cls, "from_dict", from_dict)
    return cls
