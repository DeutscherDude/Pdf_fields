import PyPDF2 as pypdf
from overwriting import insert_new_row
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


if __name__ == '__main__':


    pdf_object = open('Ex_pdf.pdf', 'rb')
    pdf = pypdf.PdfFileReader(pdf_object)
    
    answers_dict = pdf.getFormTextFields()

    insert_new_row(list(answers_dict.values()), "test.xlsx")


    # row = 1
    # col = 0

    # workbook = xlsxwriter.Workbook('test.xlsx')
    # worksheet = workbook.add_worksheet()
    # bold = workbook.add_format({'bold': 1})

    # for key, value in answers_dict.items():
    #     worksheet.write(0, col, key, bold)
    #     col += 1

    # col = 0

    # for key, value in answers_dict.items():
    #     print(f"{key}: {value}")
    #     worksheet.write_string(row, col, value)
    #     col += 1

    # workbook.close()

    # xfa = findInDict('/XFA', pdf.resolvedObjects)
    