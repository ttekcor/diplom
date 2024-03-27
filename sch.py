import pandas as pd
import openpyxl

op = pd.read_excel(r'diplom-master\Расписание весна 23-24 (16.03.2024).xlsx')
    
    #return print(op.iloc[:, :n+1])
above_35 = op[op['Дата'] == "12.03.2024"]
tmp = pd.DataFrame(op,columns = ['Учебная_группа'])
#print("!\n",tmp)
#uni = pd.unique(pd.Series(tmp))

above_36 = above_35[above_35['Учебная_группа'] == "Б5120-58.03.01кит"]
#new_op = pd.DataFrame(op, columns=[['TimeBegin'],["Дата":"12.03.2024"]])
#new_op= op.Время_начала.unique()
print(above_36.to_string())
print(len(tmp.Учебная_группа.unique ()))

