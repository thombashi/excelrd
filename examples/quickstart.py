#!/usr/bin/env python3


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


if __name__ == "__main__":
    main()
