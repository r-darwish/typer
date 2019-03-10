#!/usr/bin/env python
import os
from typing import Dict, Any, List

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about: Dict[str, Any] = {}

with open(os.path.join(here, "typer", "__version__.py")) as f:
    exec(f.read(), about)  # pylint: disable=exec-used

required: List[str] = []

setup(
    name="typer",
    version=about["__version__"],
    description="Turn dictionaries into dataclasses.",
    long_description=(os.path.join(here, "README.md")),
    long_description_content_type="text/markdown",
    author="Roey Darwish Dror",
    author_email="roey.ghost@gmail.com",
    url="https://github.com/r-darwish/typer",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"": ["LICENSE"]},
    python_requires=">=3.6",
    install_requires=required,
    extras_require={
        "test": [
            "pytest",
            "pytest-mypy",
            "pytest-flake8",
            "dataclasses; python_version<'3.7'",
            "black==18.9b0",
        ]
    },
    include_package_data=True,
    license="GPL3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
