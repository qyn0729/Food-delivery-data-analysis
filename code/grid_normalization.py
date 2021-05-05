import csv
import time
from itertools import islice
import math

# # destination normalization
# csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\destination_count.csv"))
# data = []
#
# index = 0
# for row in csv_reader:
#     index += 1
#     data.append(row)
#     if index == 2:
#         break
#
# for row in csv_reader:
#     print(len(row))
#     x = int(row[0])
#     y = int(row[1])
#     tmp = []
#     tmp.append(x)
#     tmp.append(y)
#     min = 1000000
#     max = -1000000
#     for i in range(2, len(row)):
#         if float(row[i]) < min:
#             min = float(row[i])
#         if float(row[i]) > max:
#             max = float(row[i])
#     for i in range(2, len(row)):
#         if max-min != 0:
#             tmp.append((float(row[i]) - min) / (max - min))
#         else:
#             tmp.append(0)
#     data.append(tmp)
#
# with open(r"D:\aMyFile\Data\Takeout\MyData\mine\normalized_destination_count.csv","w", encoding='UTF-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in data:
#         writer.writerow(row)


# # ---------------------
# # od normalization
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\od_count.csv"))
data = []

index = 0
for row in csv_reader:
    index += 1
    data.append(row)
    if index == 2:
        break

for row in csv_reader:
    print(len(row))
    x = int(row[0])
    y = int(row[1])
    tmp = []
    tmp.append(x)
    tmp.append(y)
    min = 1000000
    max = -1000000
    for i in range(2, len(row)):
        if float(row[i]) < min:
            min = float(row[i])
        if float(row[i]) > max:
            max = float(row[i])
    for i in range(2, len(row)):
        if max-min != 0:
            tmp.append((float(row[i]) - min) / (max - min))
        else:
            tmp.append(0)
    data.append(tmp)

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\normalized_od_count.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)