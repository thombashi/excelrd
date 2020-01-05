import sys
import unittest
from io import StringIO

from excelrd import biffh


class TestHexDump(unittest.TestCase):
    def test_hex_char_dump(self):
        sio = StringIO()
        biffh.hex_char_dump(b"abc\0e\01", 0, 6, fout=sio)
        s = sio.getvalue()
        assert "61 62 63 00 65 01" in s, s
        assert "abc~e?" in s, s


if __name__ == "__main__":
    unittest.main()
