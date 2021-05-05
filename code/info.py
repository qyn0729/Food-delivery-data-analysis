import csv
from itertools import islice
import time
from math import radians, cos, sin, asin, sqrt
import datetime
import math

def transformLat(x, y):
        ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y+ 0.2 * math.sqrt(abs(x));
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0;
        ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0;
        ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0;
        return ret;

def transformLon(x, y):
        ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x));
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0;
        ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0;
        ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0;
        return ret;

def transform(lat, lon):
    ee = 0.00669342162296594323
    a = 6378245.0
    dLat = transformLat(lon - 105.0, lat - 35.0)
    dLon = transformLon(lon - 105.0, lat - 35.0)
    radLat = lat / 180.0 * math.pi;
    magic = math.sin(radLat);
    magic = 1 - ee * magic * magic;
    sqrtMagic = math.sqrt(magic);
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi);
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi);
    mgLat = lat + dLat;
    mgLon = lon + dLon;
    return [mgLat, mgLon];

def gcj02_To_Gps84(lat, lon):
    gps = transform(lat, lon);
    lontitude = lon * 2 - gps[1];
    latitude = lat * 2 - gps[0];
    return [latitude, lontitude]

def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\part-00000-2c7df0c8-05f0-4fec-9bee-fe88ff67f7a9-c000.csv", encoding='UTF-8'))

strValue = "2017-07-28 00:00:00"
d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
t = d.timetuple()
mintime = int(time.mktime(t))*1000
strValue = "2017-09-27 00:00:00"
d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
t = d.timetuple()
maxtime = int(time.mktime(t))*1000

ids = {}
data = []
for row in islice(csv_reader, 1, None):
    #2017.7.28 - 2017.9.26
    if float(row[1]) < mintime or float(row[1]) >= maxtime:
        continue
    if float(row[5]) < mintime or float(row[5]) >= maxtime:
        continue
    orderid = row[0]
    if not ids.__contains__(orderid):
        ids[orderid] = 1
    else:
        continue
    timeArray = time.localtime(float(row[1]) / 1000)
    leave_week = timeArray.tm_wday + 1
    leavetime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    if row[2] != row[6]:
        print(row)
    # mars to 84
    leave_latitude = float(row[3])
    leave_longitude = float(row[4])
    gps = gcj02_To_Gps84(leave_latitude, leave_longitude)
    leave_latitude = gps[0]
    leave_longitude = gps[1]
    timeArray = time.localtime(float(row[5]) / 1000)
    finish_week = timeArray.tm_wday + 1
    finishtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    #mars to 84
    finish_latitude = float(row[7])
    finish_longitude = float(row[8])
    gps = gcj02_To_Gps84(finish_latitude, finish_longitude)
    finish_latitude = gps[0]
    finish_longitude = gps[1]
    duration = int(float(row[5]) / 1000 - float(row[1]) / 1000)
    distance = haversine(leave_longitude, leave_latitude, finish_longitude, finish_latitude)
    data.append([orderid, leavetime, leave_week, leave_longitude, leave_latitude, finishtime, finish_week, finish_longitude, finish_latitude, duration, distance])

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\deliver_OD.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Order ID', 'Departure Datetime', 'Departure Weekday', 'Departure lon', 'Departure lat', 'Arrival Datetime', 'Arrival Weekday', 'Arrival lon', 'Arrival lat', 'Duration', 'Distance'])
    for row in data:
        writer.writerow(row)


