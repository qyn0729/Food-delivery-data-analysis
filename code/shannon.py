import csv
import time
from itertools import islice
import math

grid_cluster_num = 2
count = {}
tazids = []

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\taz_area.csv"))
for row in islice(csv_reader, 1, None):
    id = int(row[0])
    tazids.append(id)

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\shannon\taz_grid_d"+str(grid_cluster_num)+".csv"))
for row in islice(csv_reader, 1, None):
    id = int(row[2])
    if not count.__contains__(id):
        count[id] = [0]*grid_cluster_num
    if len(row[6]) > 0:
        kclass = int(row[6][8:])-1
        count[id][kclass] += 1

shannon = {}
for id in tazids:
    tmp = 0
    total_cnt = sum(count[id])
    for i in range(grid_cluster_num):
        if count[id][i] > 0:
            tmp -= (count[id][i]/total_cnt)*math.log2(count[id][i]/total_cnt)
    shannon[id] = tmp

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\shannon\shannon_grid_d"+str(grid_cluster_num)+".csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['tazid', 'shannon'])
    for id in shannon:
        writer.writerow([id, shannon[id]])