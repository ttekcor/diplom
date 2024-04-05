import pandas as pd
import numpy as np
import openpyxl
import time
from progress.bar import IncrementalBar
import folium
from folium.plugins import MarkerCluster
def color_change(elev : dict,key):
    if(elev[key] < 5):
        return('green')
    elif(5 <= elev[key] <30):
        return('orange')
    else:
        return('red')
op = pd.read_csv('diplom\Расписание весна 23-24 (16.03.2024)1.csv',on_bad_lines='skip',sep=";")
print(op)
    
    #return print(op.iloc[:, :n+1])
above_35 = pd.DataFrame(op[op['Дата'] == "12.03.2024"])
print("?",above_35)
#tmp = pd.DataFrame(above_35,columns = ['Учебная_группа'])

tmp_corpus = pd.DataFrame(above_35,columns = ['Аудитория'])
bar = IncrementalBar('Countdown', max = len(tmp_corpus))
print("!\n",tmp_corpus)
tmp_ = tmp_corpus.Аудитория.unique ()
#tmp_ = np.split(tmp_, " ")
print(len(list(tmp_)))
#uni = pd.unique(pd.Series(tmp))
groups_dict = {}
tmp_set = set([x[0] for x in tmp_])
print(tmp_set)
for i in tmp_set:
    groups_dict[i] = 0
print(groups_dict)
for x in tmp_:
    if x[0] in groups_dict : 
        groups_dict[x[0]] += 1
for key in groups_dict:        
    color_change(groups_dict,key)
    print(f"{key} is {color_change(groups_dict,key)}")
#     bar.next()
#     time.sleep(1)
#     above_36 = above_35[above_35['Учебная_группа'] == tmp]
#new_op = pd.DataFrame(op, columns=[['TimeBegin'],["Дата":"12.03.2024"]])
#new_op= op.Время_начала.unique()
#print(above_36.to_string())
#print(len(tmp.Учебная_группа.unique ()))
#     time_out = pd.DataFrame(above_36,columns = ["Время окончания"]).max(skipna=False)
#     time_in = pd.DataFrame(above_36,columns = ["Время_начала"]).min(skipna=False)
#     tmp_list = []
#     tmp_list.append(time_in)
#     tmp_list.append(time_out)
#     groups_dict[x] = tmp_list
# bar.finish()
# print(groups_dict)
corpus_dict = {'G':[43.026203, 131.887991],
               'A':[43.024578, 131.894033],
               'B':[43.024728, 131.892108],
               'C':[43.024264, 131.894695],
               'D':[43.025380, 131.890997],
               'E':[43.023989, 131.895874],
               'F':[43.023978, 131.898122],
               'L':[43.024405, 131.886959],
               'S':[43.026234, 131.889964]}
# for i in corpus_dict:
#     if i in groups_dict:
#         corpus_dict[i].append(groups_dict[i])
# print(corpus_dict)

map = folium.Map(location=[43.026188,131.8911495], zoom_start = 16, tiles='CartoDB dark_matter')
marker_cluster = MarkerCluster().add_to(map)


for coordinates in corpus_dict:
    if coordinates in groups_dict:
        folium.CircleMarker(location=corpus_dict[coordinates],raduis = 10, popup=str(groups_dict[coordinates])+" Количество пар", fill_color=color_change(groups_dict,coordinates), color="gray", fill_opacity = 5).add_to(marker_cluster)

map.save("diplom\map1.html")

