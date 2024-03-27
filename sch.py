import pandas as pd
import openpyxl

op = pd.read_excel(r"C:\Users\curvh\Downloads\Telegram Desktop\Расписание весна 23-24 (16.03.2024).xlsx")
    
    #return print(op.iloc[:, :n+1])
    
new_op = pd.DataFrame(op, columns=['Время_начала'])
#new_op= op.Время_начала.unique()
print(new_op)

