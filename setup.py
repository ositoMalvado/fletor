from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Streaming video data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="fletor",
    version="0.0.1b",
    author="ositoMalvado (Julián Perez)",
    author_email="<mordecaaii@gmail.com>",
    url="https://github.com/ositoMalvado/fletor",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['flet', 'collections'],
    keywords=['flet', 'component', 'flet component', 'custom flet', 'useful component', 'ositomalvado'],
    classifiers=[
        "Development Status :: 1 - Starting",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)