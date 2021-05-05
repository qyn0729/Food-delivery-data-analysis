# coding:utf-8
import os
import csv
import arcpy
from itertools import islice

def draw_kmedoids(type, cluster_num):
    xs = []
    ys = []
    xmin = 0
    ymin = 0
    csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\\"+type+"_count.csv"))
    for row in csv_reader:
        xmin = float(row[0])
        ymin = float(row[1])
        break
    csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\\"+type+"_count.csv"))
    for row in islice(csv_reader, 2, None):
        xs.append(int(row[0]))
        ys.append(int(row[1]))

    if type == 'od':
        csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_od"+str(cluster_num)+".csv"))
        path = r'D:\\aMyFile\\Data\\Takeout\\MyData\\mine\\kmedoids\\grid\\shp\\'
        outputname = "grid_od"+str(cluster_num)+".shp"
        dir = path + outputname;
    else:
        csv_reader = csv.reader(
            open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_d" + str(cluster_num) + ".csv"))
        path = r'D:\\aMyFile\\Data\\Takeout\\MyData\\mine\\kmedoids\\grid\\shp\\'
        outputname = "grid_d" + str(cluster_num) + ".shp"
        dir = path + outputname;

    spatRef = arcpy.SpatialReference(4326)
    createFC = arcpy.CreateFeatureclass_management(os.path.dirname(dir), os.path.basename(dir), "POLYGON", "", "", "",spatRef)
    # 创建字段
    arcpy.AddField_management(createFC, "kclass", "TEXT")

    cur = arcpy.InsertCursor(createFC)
    index = 0
    for item in csv_reader:
        array = arcpy.Array()
        kclass = 'Cluster '+ str(int(item[0])+1)
        print(kclass)
        # minX = 119.980622 + ys[index] * 0.001
        # minY = 30.121932 + xs[index] * 0.001
        # maxX = 119.980622 + (ys[index] + 1) * 0.001
        # maxY = 30.121932 + (xs[index] + 1) * 0.001
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
        row.kclass = kclass

        cur.insertRow(row)
        index += 1

    print 'finished'

draw_kmedoids('destination', 3)

