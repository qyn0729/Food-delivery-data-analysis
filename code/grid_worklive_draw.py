# coding:utf-8
import os
import csv
import arcpy
from itertools import islice

xmin = 0
ymin = 0
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\destination_count.csv"))
for row in csv_reader:
    xmin = float(row[0])
    ymin = float(row[1])
    break

type = ['work', 'live']
for i in range(2):
    cur_type = type[i]
    xs = []
    ys = []
    csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\work_live\\" + cur_type + "place_order_cnt_d2.csv"))
    for row in islice(csv_reader, 1, None):
        xs.append(int(float(row[0])))
        ys.append(int(float(row[1])))
    csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\work_live\\" + cur_type + "place_order_cnt_d2.csv"))
    path = r'D:\\aMyFile\Data\\Takeout\\MyData\\mine\\analysis\\work_live\\shp\\'
    outputname = cur_type+"place_order_cnt_d2.shp"
    dir = path + outputname;

    spatRef = arcpy.SpatialReference(4326)
    createFC = arcpy.CreateFeatureclass_management(os.path.dirname(dir), os.path.basename(dir), "POLYGON", "", "", "",spatRef)
    # 创建字段
    if cur_type == 'work':
        arcpy.AddField_management(createFC, "work", "FLOAT")
        arcpy.AddField_management(createFC, "extrawork", "FLOAT")
        arcpy.AddField_management(createFC, "work_sat", "FLOAT")
        arcpy.AddField_management(createFC, "work_sun", "FLOAT")
    else:
        arcpy.AddField_management(createFC, "live", "FLOAT")
        arcpy.AddField_management(createFC, "wd_supper", "FLOAT")
        arcpy.AddField_management(createFC, "wk_supper", "FLOAT")
    arcpy.AddField_management(createFC, "x", "FLOAT")
    arcpy.AddField_management(createFC, "y", "FLOAT")

    cur = arcpy.InsertCursor(createFC)
    index = 0
    for item in islice(csv_reader, 1, None):
        array = arcpy.Array()
        minX = xmin + xs[index] * 0.001
        minY = ymin + ys[index] * 0.001
        maxX = xmin + (xs[index] + 1) * 0.001
        maxY = ymin + (ys[index] + 1) * 0.001

        pointLB = arcpy.Point()
        pointLB.X = minX
        pointLB.Y = minY

        pointRB = arcpy.Point()
        pointRB.X = maxX
        pointRB.Y = minY

        pointRU = arcpy.Point()
        pointRU.X = maxX
        pointRU.Y = maxY

        pointLU = arcpy.Point()
        pointLU.X = minX
        pointLU.Y = maxY

        array.append(pointLB)
        array.append(pointRB)
        array.append(pointRU)
        array.append(pointLU)

        row = cur.newRow()
        row.shape = array
        if cur_type == 'work':
            row.work = float(item[2])
            row.extrawork = float(item[3])
            row.work_sat = float(item[4])
            row.work_sun = float(item[5])
        else:
            row.live = float(item[2])
            row.wd_supper = float(item[3])
            row.wk_supper = float(item[4])
        row.x = xs[index]
        row.y = ys[index]

        cur.insertRow(row)
        index += 1

    print 'finished'