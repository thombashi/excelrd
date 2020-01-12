import sys

from setuptools import setup

from excelrd.info import __VERSION__


MODULE_NAME = "excelrd"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
TESTS_REQUIRES = ["pytest"]


def pytest_runner_requires() -> list:
    if set(["pytest", "test", "ptr"]).intersection(sys.argv):
        return ["pytest-runner"]

    return []


def get_release_command_class():
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open("README.rst") as fp:
    long_description = fp.read()


setup(
    name=MODULE_NAME,
    version=__VERSION__,
    author="John Machin",
    author_email="sjmachin@lexicon.net",
    maintainer="Tsuyoshi Hombashi",
    maintainer_email="tsuyoshi.hombashi@gmail.com",
    url="https://github.com/thombashi/excelrd",
    packages=["excelrd"],
    scripts=["scripts/runxlrd.py",],
    description=(
        "Library for developers to extract data from Microsoft Excel (tm) spreadsheet files"
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="BSD",
    keywords=["xls", "excel", "spreadsheet", "workbook"],
    python_requires=">=3.5",
    setup_requires=pytest_runner_requires(),
    tests_require=TESTS_REQUIRES,
    extras_require={
        "dev": ["releasecmd>=0.2.0,<1", "twine", "wheel"] + ["pylama"] + TESTS_REQUIRES,
        "test": TESTS_REQUIRES,
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass=get_release_command_class(),
)
