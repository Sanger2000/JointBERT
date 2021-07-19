import setuptools
import pathlib
from setuptools import setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="JointBERT",
    version="0.0.1",
    author="Aman",
    author_email="aman@you.com",
    description="Joint BERT models for Intent Classification and Slot Filling",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://https://github.com/monologg/JointBERT",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
