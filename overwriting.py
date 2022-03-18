import openpyxl
from openpyxl.reader.excel import load_workbook


def insert_new_row(values: list[str], file_name: str) -> None:
    wb = load_workbook(filename = file_name)
    ws = wb['Sheet1']
    row = ws.max_row + 1

    for col, entry in enumerate(values, start = 1):
        ws.cell(row = row, column = col, value = entry)

    wb.save(file_name)

