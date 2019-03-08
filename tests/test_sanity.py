from typer import from_dict

from dataclasses import dataclass


@dataclass
@from_dict
class Data:
    number: int
    name: str


def test_sanity():
    instance = Data.from_dict({'number': 1, 'name': "hi"})
    assert isinstance(instance, Data)
    assert instance.number == 1
    assert instance.name == "hi"
