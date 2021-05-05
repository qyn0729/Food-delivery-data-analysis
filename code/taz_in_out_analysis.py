import csv
import time
from itertools import islice
import math
import xlwt

taz_area = {}
tazids = []
in_out = {}

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\taz_area.csv"))
for row in islice(csv_reader, 1, None):
    id = int(row[0])
    area = float(row[1])
    taz_area[id] = area/1000000
    tazids.append(id)

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\taz_od_count.csv"))
for row in islice(csv_reader, 1, None):
    tazid = int(row[0])
    in_out[tazid] = [0]*72
    for i in range(72):
        in_out[tazid][i] = float(row[i+73]) - float(row[i+1])


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Sheet1')


label = ['tazid']
for i in range(24):
    label.append('weekday_in_out '+str(i))
for i in range(24):
    label.append('sat_in_out '+str(i))
for i in range(24):
    label.append('sun_in_out '+str(i))
for i in range(len(label)):
    worksheet.write(0, i, label[i])

for k in range(len(tazids)):
    id = tazids[k]
    worksheet.write(k+1, 0, id)
    for i in range(72):
        worksheet.write(k+1, i+1, in_out[id][i])

workbook.save(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\in_out\taz_in_out.xls")