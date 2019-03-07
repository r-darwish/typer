#!/usr/bin/env python
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}

with open(os.path.join(here, "typer", "__version__.py")) as f:
    exec(f.read(), about) # pylint: disable=exec-used

required = []

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
    python_requires=">=3.5",
    install_requires=required,
    extras_require={"test": ["pytest", "mypy", "pylint", "dataclasses; python_version<'3.7'"]},
    include_package_data=True,
    license="GPL3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
