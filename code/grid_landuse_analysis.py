import csv
from itertools import islice
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np



cluster_num = 2
area = []
sum_area = [0]*cluster_num
names = {}
count = [0]*cluster_num

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_d"+str(cluster_num)+".csv"))
for row in csv_reader:
    count[int(row[0])] += 1

for i in range(cluster_num):
    area.append(dict())
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\landuse\grid\true_landuse_destination"+str(cluster_num)+".csv", encoding='gbk'))
for row in islice(csv_reader, 1, None):
    name = row[2]
    if name != 'Green' and name != 'Other':
        names[name] = 1
        kclass = int(row[1][8])-1
        area[kclass][name] = float(row[0])
        sum_area[kclass] += float(row[0])

data = []
for i in range(cluster_num):
    tmp = []
    tmp.append('Cluster' + str(i+1))
    tmp.append(count[i])
    for item in names:
        if area[i].__contains__(item):
            tmp.append(area[i][item]/sum_area[i])
        else:
            tmp.append(0)
    data.append(tmp)

print(data)

csvFile = open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\landuse\grid\true_destination"+str(cluster_num)+"_analysis.csv",'w',newline='',encoding='utf-8-sig')
writer = csv.writer(csvFile)
tmp = ['', 'count']
for item in names:
    tmp.append(item)
writer.writerow(tmp)
for row in data:
    writer.writerow(row)

