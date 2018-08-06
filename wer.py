
from openpyxl import Workbook

boo= Workbook()
sheet=boo.active
sheet.cell(row= 1,column=1).value = 'Number of pecks'
boo.save('file_name')
