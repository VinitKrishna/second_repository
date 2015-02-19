import xlrd 
from datetime import datetime

workbook = xlrd.open_workbook("D:\Be Natural outdoor 2012.xlsx")
sheet = ["Raw data"]
worksheet = workbook.sheet_by_name(sheet[0])
lDate = datetime(*xlrd.xldate_as_tuple(worksheet.cell_value(1, 5), workbook.datemode))
print lDate
lDayString = lDate.strftime('%Y-%m-%d')
print lDayString
