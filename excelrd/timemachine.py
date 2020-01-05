##
# <p>Copyright (c) 2006-2012 Stephen John Machin, Lingfo Pty Ltd</p>
# <p>This module is part of the excelrd package, which is released under a BSD-style licence.</p>
##

# timemachine.py -- adaptation for single codebase.
# Currently supported: 2.6 to 2.7, 3.2+
# usage: from timemachine import *

import sys
from io import BytesIO as BYTES_IO


BYTES_LITERAL = lambda x: x.encode("latin1")
UNICODE_LITERAL = lambda x: x
BYTES_ORD = lambda byte: byte


def fprintf(f, fmt, *vargs):
    fmt = fmt.replace("%r", "%a")
    if fmt.endswith("\n"):
        print(fmt[:-1] % vargs, file=f)
    else:
        print(fmt % vargs, end=" ", file=f)


EXCEL_TEXT_TYPES = (str, bytes, bytearray)  # xlwt: isinstance(obj, EXCEL_TEXT_TYPES)
REPR = ascii
ensure_unicode = lambda s: s
