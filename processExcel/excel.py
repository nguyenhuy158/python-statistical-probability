import openpyxl


def get_value_excel(filename, cellname):
    workbook = openpyxl.load_workbook(filename)
    sheet_1 = workbook['Sheet1']
    workbook.close()
    return sheet_1[cellname].value

def updata_value_excel(filename, cellnam, data):
    workbook = openpyxl.load_workbook(filename)
    sheet_1 = workbook['Sheet1']
    sheet_1[cellnam].value = data
    workbook.close()
    workbook.save(filename)

filename = r"C:\Users\Python\Desktop\code\tool excel\data.xlsx"
cellname = "H1"

print(f"value data {cellname}: " + get_value_excel(filename, cellname))

cellname = input("selecte cell: ")
data = input(f"data replace cell {cellname}: ")

updata_value_excel(filename, cellname, data)


