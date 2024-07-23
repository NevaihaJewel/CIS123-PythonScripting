from openpyxl import Workbook
import datetime

book = Workbook()
sheet = book.active

sheet['A1'] = 'nevada3921'

sheet['A2'] = 23
sheet['A3'] = 45
sheet['A4'] = '=A2+A3'

now = datetime.datetime.now()
sheet['A5'] = now

book.save("C:\\Users\\nevai\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\FirstExcel.xlsx")
