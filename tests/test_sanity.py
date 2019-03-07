import sys
from typer import from_dict

if sys.version_info.minor < 7:
    from dataclasses import dataclass


def test_sanity():
    pass
