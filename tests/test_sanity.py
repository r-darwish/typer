from typer import from_dict

from dataclasses import dataclass


@dataclass
class Data:
    number: int
    name: str


def test_sanity() -> None:
    instance = from_dict(Data, {"number": 1, "name": "hi"})
    assert isinstance(instance, Data)
    assert instance.number == 1
    assert instance.name == "hi"
