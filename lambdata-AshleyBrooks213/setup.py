"""
lambdata - a collection of Data Science functions
"""

import setuptools # available in the standard library

REQUIRED = [
    "numpy",
    "pandas"
]

with open(README.md, "r") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="lambdata-AshleyBrooks213", 
    version="0.0.1",
    owner="AshleyBrooks213",
    description=LONG_DESCRIPTION, 
    long_descriptions_content="test/markdown",
    #how we want to find our REQUIRED packages
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)