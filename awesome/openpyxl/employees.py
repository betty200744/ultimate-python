from openpyxl import load_workbook


# write workbook
def write_employees():
    print("read employees")
    # workbook
    wb = load_workbook(filename="employees.xlsx")
    # work sheet
    ws1 = wb['Sheet1']
    # max_row, max_col
    max_row = ws1.max_row
    new_col = (100999, 19604, 'Georgi', 'Facello', 'M', 31589)
    for i, v in enumerate(new_col):
        ws1.cell(row=max_row + 1, column=i + 1, value=v)
    wb.save(filename="employees.xlsx")


# read workbook
def read_employees():
    # workbook
    wb = load_workbook(filename='employees.xlsx')

    # work sheet
    for sheet in wb:
        print(sheet.title)
    ws1 = wb['Sheet1']
    print(ws1)

    # ws1 row 0
    print("row1 ", ws1[1])
    # ws1 row 1 cell A
    print("A1", ws1['A1'].value)

    # row, only print row 0
    for i, row in enumerate(ws1.iter_rows(values_only=True)):
        if i == 0:
            print("row0:", row)
            # cell, only print cell 0
            print("row0, cell0:", row[0])

    # columns, only print column 0
    for i, col in enumerate(ws1.iter_cols(values_only=True)):
        if i == 0:
            print("column0:", col)
            # cell, only print cell 0
            print("column0, cell0:", col[0])


if __name__ == '__main__':
    print("main")
    write_employees()
