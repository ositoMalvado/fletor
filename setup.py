from setuptools import setup, find_packages

description = """
Flet components library

This library provides a set of components that can be used in Flet applications.

**Fletor**
"""

setup(
    name="fletor",
    version="1.0.0b",
    author="Julián Perez",
    author_email="mordecaaii@gmail.com",
    description="Useful flet components",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["flet"],
    python_requires=">=3.8",
    project_urls={
        "support": "https://ositomalvado.github.io/",
        "repository": "https://github.com/ositoMalvado/fletor",
        "tracker": "https://github.com/ositoMalvado/fletor/issues",
    },
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)