[![Build Status](https://travis-ci.org/thombashi/excelrd.svg?branch=master)](https://travis-ci.org/thombashi/excelrd)
[![Coverage Status](https://coveralls.io/repos/github/thombashi/excelrd/badge.svg?branch=master)](https://coveralls.io/github/thombashi/excelrd?branch=master)
[![Documentation Status](https://readthedocs.org/projects/xlrd/badge/?version=latest)](http://xlrd.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/excelrd.svg)](https://badge.fury.io/py/excelrd)

### excelrd

**Purpose**: Provide a library for developers to use to extract data from Microsoft Excel (tm) spreadsheet files. It is not an end-user tool.

**Author**: John Machin

**Licence**: BSD-style (see licences.py)

**Versions of Python supported**: 3.5+.

**Outside scope**: excelrd will safely and reliably ignore any of these if present in the file:

*   Charts, Macros, Pictures, any other embedded object. WARNING: currently this includes embedded worksheets.
*   VBA modules
*   Formulas (results of formula calculations are extracted, of course).
*   Comments
*   Hyperlinks
*   Autofilters, advanced filters, pivot tables, conditional formatting, data validation
*   Handling password-protected (encrypted) files.

**Quick start**:

```python
import xlrd

book = xlrd.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
    print(sh.row(rx))
```

**Another quick start**: This will show the first, second and last rows of each sheet in each file:

    python PYDIR/scripts/runxlrd.py 3rows *blah*.xls

**Acknowledgements**:

*   This package started life as a translation from C into Python of parts of a utility called "xlreader" developed by David Giffin. "This product includes software developed by David Giffin <david@giffin.org>."
*   OpenOffice.org has truly excellent documentation of the Microsoft Excel file formats and Compound Document file format, authored by Daniel Rentz. See http://sc.openoffice.org
*   U+5F20 U+654F: over a decade of inspiration, support, and interesting decoding opportunities.
*   Ksenia Marasanova: sample Macintosh and non-Latin1 files, alpha testing
*   Backporting to Python 2.1 was partially funded by Journyx - provider of timesheet and project accounting solutions (http://journyx.com/).
*   Provision of formatting information in version 0.6.1 was funded by Simplistix Ltd (http://www.simplistix.co.uk/)
