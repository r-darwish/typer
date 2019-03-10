import pytest
from typer import from_dict, MissingAnnotations, TypificationError
from dataclasses import dataclass


@dataclass
class Data:
    number: int
    name: str


class NoAnnotations:
    x = 1


def test_sanity() -> None:
    instance = from_dict(Data, {"number": 1, "name": "hi"})
    assert isinstance(instance, Data)
    assert instance.number == 1
    assert instance.name == "hi"


def test_missing_field() -> None:
    with pytest.raises(TypificationError):
        from_dict(Data, {"number": 1})


def test_no_annotations() -> None:
    with pytest.raises(MissingAnnotations):
        from_dict(NoAnnotations, {"number": 1, "name": "hi"})
