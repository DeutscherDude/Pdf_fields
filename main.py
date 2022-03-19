import PyPDF2 as pypdf
from overwriting import insert_new_row, insert_to_cells
import xlsxwriter

def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value, dict):
            x = findInDict(needle, value)
            if x is not None:
                return x

dest_cells = ['B3', 'B6', 'C10', 'C14', 'C17', 'C20', 'C22', 'C24']

if __name__ == '__main__':


    pdf_object = open('form.pdf', 'rb')
    pdf = pypdf.PdfFileReader(pdf_object)
    
    answers_dict = pdf.getFormTextFields()

    # all_fields_dict = pdf.getFields()
    # to_delete = ['FT', '/Tx', '/T', '/TU', '/V', '/DV']

    insert_new_row(list(answers_dict.values()), "test.xlsx")
    insert_to_cells(list(answers_dict.values()), "test.xlsx", dest_cells)
    pdf_object.close()
