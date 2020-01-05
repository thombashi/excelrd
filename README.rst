.. contents:: **excelrd**
   :backlinks: top
   :depth: 2

.. image:: https://badge.fury.io/py/excelrd.svg
    :target: https://badge.fury.io/py/excelrd
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/excelrd.svg
    :target: https://pypi.org/project/excelrd
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/thombashi/excelrd/master.svg?label=CI
    :target: https://travis-ci.org/thombashi/excelrd
    :alt: CI status

.. image:: https://coveralls.io/repos/github/thombashi/excelrd/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/excelrd?branch=master
    :alt: Test coverage

excelrd
==================
``excelrd`` is a modified version of `xlrd <http://www.python-excel.org/>`__ to work for the latest Python.

**Purpose**: Provide a library for developers to use to extract data from Microsoft Excel (tm) spreadsheet files. It is not an end-user tool.

**Author**: John Machin

**Licence**: BSD-style (see licences.py)

**Versions of Python supported**: 3.5+.

**Outside scope**: excelrd will safely and reliably ignore any of these
if present in the file:

-  Charts, Macros, Pictures, any other embedded object. WARNING:
   currently this includes embedded worksheets.
-  VBA modules
-  Formulas (results of formula calculations are extracted, of course).
-  Comments
-  Hyperlinks
-  Autofilters, advanced filters, pivot tables, conditional formatting,
   data validation
-  Handling password-protected (encrypted) files.


Quick start
==================
:Sample Code:
    .. code:: python

        import excelrd


        def main():
            book = excelrd.open_workbook("namesdemo.xls")

            print("The number of worksheets is {}".format(book.nsheets))
            print("Worksheet name(s): {}".format(", ".join(book.sheet_names())))

            sh = book.sheet_by_index(2)
            print("{}: rows={}, cols={}".format(sh.name, sh.nrows, sh.ncols))

            for row_idx in range(sh.nrows):
                for col_idx in range(sh.ncols):
                    cell = sh.cell(row_idx, col_idx)

                    if not cell.value:
                        continue

                    print("row={}, col={}, value={}".format(row_idx, col_idx, cell.value))

Another quick start
---------------------------
This will show the first, second and last rows
of each sheet in each file:

::

    python PYDIR/scripts/runxlrd.py 3rows *blah*.xls


Acknowledgements
====================================
-  This package started life as a translation from C into Python of
   parts of a utility called "xlreader" developed by David Giffin. "This
   product includes software developed by David Giffin
   david@giffin.org."
-  OpenOffice.org has truly excellent documentation of the Microsoft
   Excel file formats and Compound Document file format, authored by
   Daniel Rentz. See http://sc.openoffice.org
-  U+5F20 U+654F: over a decade of inspiration, support, and interesting
   decoding opportunities.
-  Ksenia Marasanova: sample Macintosh and non-Latin1 files, alpha
   testing
-  Backporting to Python 2.1 was partially funded by Journyx - provider
   of timesheet and project accounting solutions (http://journyx.com/).
-  Provision of formatting information in version 0.6.1 was funded by
   Simplistix Ltd (http://www.simplistix.co.uk/)
