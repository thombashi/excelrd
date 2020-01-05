import sys

from setuptools import setup

from excelrd.info import __VERSION__


def pytest_runner_requires() -> list:
    if set(["pytest", "test", "ptr"]).intersection(sys.argv):
        return ["pytest-runner"]

    return []

TESTS_REQUIRES = ["pytest"]

setup(
    name = 'excelrd',
    version = __VERSION__,
    author = 'John Machin',
    author_email = 'sjmachin@lexicon.net',
    url = 'http://www.python-excel.org/',
    packages = ['excelrd'],
    scripts = [
        'scripts/runxlrd.py',
    ],
    description = (
        'Library for developers to extract data from '
        'Microsoft Excel (tm) spreadsheet files'
    ),
    long_description = (
        "Extract data from Excel spreadsheets "
        "(.xls and .xlsx, versions 2.0 onwards) on any platform. "
        "Pure Python (2.7, 3.4+). "
        "Strong support for Excel dates. Unicode-aware."
    ),
    platforms = ["Any platform -- don't need Windows"],
    license = 'BSD',
    keywords = ['xls', 'excel', 'spreadsheet', 'workbook'],
    python_requires=">=3.5",
    setup_requires=pytest_runner_requires(),
    tests_require=TESTS_REQUIRES,
    extras_require={
        "test": TESTS_REQUIRES,
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
