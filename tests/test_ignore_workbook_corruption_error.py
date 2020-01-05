from unittest import TestCase

import excelrd

from .base import from_this_dir


class TestIgnoreWorkbookCorruption(TestCase):
    def test_not_corrupted(self):
        with self.assertRaises(Exception) as context:
            excelrd.open_workbook(from_this_dir("corrupted_error.xls"))
        self.assertTrue("Workbook corruption" in str(context.exception))

        excelrd.open_workbook(from_this_dir("corrupted_error.xls"), ignore_workbook_corruption=True)
