import csv
import time
from itertools import islice
import math


# Destination count

weekday = 0
sat = 0
sun = 0
exist_days = {}
minx = 100000
miny = 100000

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\destination_final_data.csv"))
for row in islice(csv_reader, 1, None):
    if float(row[7]) < minx:
        minx = float(row[7])
    if float(row[8]) < miny:
        miny = float(row[8])
    timeArray = time.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    if not exist_days.__contains__(str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)):
        exist_days[str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)] = 1
        if timeArray.tm_wday <= 4:
            weekday += 1
        elif timeArray.tm_wday == 5:
            sat += 1
        else:
            sun += 1

print(minx, miny)

df = []
finish = {}
maxx = 0
maxy = 0
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\destination_final_data.csv"))
for row in islice(csv_reader, 1, None):
    timeArray = time.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    if timeArray.tm_wday <= 4:
        hour = timeArray.tm_hour
        days = weekday
    elif timeArray.tm_wday == 5:
        hour = timeArray.tm_hour + 24
        days = sat
    else:
        hour = timeArray.tm_hour + 48
        days = sun
    x = int((float(row[7]) - minx)/0.001)
    y = int((float(row[8]) - miny)/0.001)
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if finish.__contains__(str(x)+'-'+str(y)+'-'+str(hour)):
        finish[str(x)+'-'+str(y)+'-'+str(hour)] += 1/days
    else:
        finish[str(x) + '-' + str(y) + '-' + str(hour)] = 1/days


data = []
for x in range(maxx):
    for y in range(maxy):
        tmp = [x, y]
        for hour in range(72):
            if finish.__contains__(str(x)+'-'+str(y)+'-'+str(hour)):
                tmp.append(finish[str(x) + '-' + str(y) + '-' + str(hour)])
            else:
                tmp.append(0)
        for i in range(2, len(tmp)):
            if tmp[i] != 0:
                data.append(tmp)
                break

print(len(data))

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\destination_count.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([minx, miny])
    label = ['x', 'y', 'weekday']
    for i in range(23):
        label.append(' ')
    label.append('sat')
    for i in range(23):
        label.append(' ')
    label.append('sun')
    writer.writerow(label)
    for row in data:
        writer.writerow(row)




# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# OD count
weekday = 0
sat = 0
sun = 0
exist_days = {}
minx = 100000
miny = 100000


csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\destination_final_data.csv"))
for row in islice(csv_reader, 1, None):
    if float(row[7]) < minx:
        minx = float(row[7])
    if float(row[8]) < miny:
        miny = float(row[8])
    timeArray = time.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    if not exist_days.__contains__(str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)):
        exist_days[str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)] = 1
        if timeArray.tm_wday <= 4:
            weekday += 1
        elif timeArray.tm_wday == 5:
            sat += 1
        else:
            sun += 1

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\origin_final_data.csv"))
for row in islice(csv_reader, 1, None):
    if float(row[3]) < minx:
        minx = float(row[3])
    if float(row[4]) < miny:
        miny = float(row[4])
    timeArray = time.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    if not exist_days.__contains__(str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)):
        exist_days[str(timeArray.tm_year)+'-'+str(timeArray.tm_mon)+'-'+str(timeArray.tm_mday)] = 1
        if timeArray.tm_wday <= 4:
            weekday += 1
        elif timeArray.tm_wday == 5:
            sat += 1
        else:
            sun += 1

print(minx, miny)

df = []
finish = {}
origin = {}
maxx = 0
maxy = 0
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\destination_final_data.csv"))
for row in islice(csv_reader, 1, None):
    timeArray = time.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    if timeArray.tm_wday <= 4:
        hour = timeArray.tm_hour
        days = weekday
    elif timeArray.tm_wday == 5:
        hour = timeArray.tm_hour + 24
        days = sat
    else:
        hour = timeArray.tm_hour + 48
        days = sun
    x = int((float(row[7]) - minx)/0.001)
    y = int((float(row[8]) - miny)/0.001)
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if finish.__contains__(str(x)+'-'+str(y)+'-'+str(hour)):
        finish[str(x)+'-'+str(y)+'-'+str(hour)] += 1/days
    else:
        finish[str(x) + '-' + str(y) + '-' + str(hour)] = 1/days

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\origin_final_data.csv"))
for row in islice(csv_reader, 1, None):
    timeArray = time.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    if timeArray.tm_wday <= 4:
        hour = timeArray.tm_hour
        days = weekday
    elif timeArray.tm_wday == 5:
        hour = timeArray.tm_hour + 24
        days = sat
    else:
        hour = timeArray.tm_hour + 48
        days = sun
    x = int((float(row[3]) - minx)/0.001)
    y = int((float(row[4]) - miny)/0.001)
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if origin.__contains__(str(x)+'-'+str(y)+'-'+str(hour)):
        origin[str(x)+'-'+str(y)+'-'+str(hour)] += 1/days
    else:
        origin[str(x) + '-' + str(y) + '-' + str(hour)] = 1/days


data = []
for x in range(maxx):
    for y in range(maxy):
        tmp = [x, y]
        for hour in range(72):
            if origin.__contains__(str(x) + '-' + str(y) + '-' + str(hour)):
                tmp.append(origin[str(x) + '-' + str(y) + '-' + str(hour)])
            else:
                tmp.append(0)
        for hour in range(72):
            if finish.__contains__(str(x)+'-'+str(y)+'-'+str(hour)):
                tmp.append(finish[str(x) + '-' + str(y) + '-' + str(hour)])
            else:
                tmp.append(0)
        for i in range(2, len(tmp)):
            if tmp[i] != 0:
                data.append(tmp)
                break

print(len(data))

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\od_count.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([minx, miny])
    label = ['x', 'y', 'origin_weekday']
    for i in range(23):
        label.append(' ')
    label.append('origin_sat')
    for i in range(23):
        label.append(' ')
    label.append('origin_sun')
    for i in range(23):
        label.append(' ')
    label.append('finish_weekday')
    for i in range(23):
        label.append(' ')
    label.append('finish_sat')
    for i in range(23):
        label.append(' ')
    label.append('finish_sun')
    writer.writerow(label)
    for row in data:
        writer.writerow(row)