import csv
from itertools import islice
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import math
import matplotlib as mpl

def poi_analysis(type, cluster_num):
    xs = []
    ys = []
    area = [0] * cluster_num
    kclass = {}
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
    else:
        csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_d" + str(cluster_num) + ".csv"))
    index = 0
    for row in csv_reader:
        kclass[str(xs[index])+'-'+str(ys[index])] = int(row[0])
        area[int(row[0])] += 1
        index += 1


    poi = []
    total_poi = [0]*16
    for i in range(cluster_num):
        poi.append([0]*16)
    poi_count = 0

    csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\poi\simple_poi.csv",encoding='utf-8', errors='ignore'))
    for row in islice(csv_reader, 1, None):
        category = int(row[1][:2]) - 11
        x = int((float(row[2])-xmin)/0.001)
        y = int((float(row[3])-ymin)/0.001)
        if kclass.__contains__(str(x)+'-'+str(y)):
            cur_kclass = kclass[str(x)+'-'+str(y)]
            poi[cur_kclass][category] += 1
            poi_count += 1
            total_poi[category] += 1

    # POI类型比例偏移（category ratio offset, CRO）
    mcr = [0]*16
    for j in range(16):
        mcr[j] = total_poi[j]/poi_count
    cro = []
    for i in range(cluster_num):
        cro.append([0]*16)
        for j in range(16):
            if mcr[j] != 0:
                cro[i][j] = (poi[i][j]/sum(poi[i]) - mcr[j])/mcr[j]
            else:
                cro[i][j] = 0
    print(cro)

    # draw
    plt.figure(1)
    plt.figure(dpi=300,figsize=(24, 8))
    # plt.figure(dpi=300)
    plt.rcParams['font.family']=['SimHei']
    for i in range(cluster_num):
        ax1 = plt.subplot(2, math.ceil(cluster_num/2), 1+i)
        # ax1 = plt.subplot(math.ceil(cluster_num / 2), 2, 1 + i)
        center = cro[i]
        ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
        colors = np.where(np.array(center) > 0, "green", "red")
        ax1.barh(range(16), center, tick_label=[u'餐饮', u'住、宿', u'批发、零售', u'汽车销售及服务', u'金融、保险', u'教育、文化', u'卫生、社保', u'运动、休闲', u'公共设施', u'商业设施、商务服务', u'居民服务', u'公司企业', u'交通运输、仓储', u'科研及技术服务', u'农林牧渔业', u'自然地物\地名'], color=colors)
        plt.grid(linestyle='--', axis ='x')
        plt.title("Cluster " + str(i + 1), fontsize=18)
    plt.savefig(r'D:\aMyFile\Data\Takeout\MyData\mine\analysis\poi\grid\\grid_'+type+str(cluster_num)+'_poi_CRO.png', bbox_inches='tight')
    plt.show()

    csvFile = open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\poi\grid\\grid_"+type+str(cluster_num)+"_poi_CRO.csv",'w',newline='',encoding='utf-8-sig')
    writer = csv.writer(csvFile)
    writer.writerow([u'餐饮', u'住、宿', u'批发、零售', u'汽车销售及服务', u'金融、保险', u'教育、文化', u'卫生、社保', u'运动、休闲', u'公共设施', u'商业设施、商务服务', u'居民服务', u'公司企业', u'交通运输、仓储', u'科研及技术服务', u'农林牧渔业', u'自然地物\地名'])
    for row in cro:
        writer.writerow(row)


    # POI 富集度
    data = []
    for i in range(cluster_num):
        tmp = []
        cur_sum = 0
        for item in poi[i]:
            cur_sum += item
        for j in range(len(poi[i])):
            if total_poi[j]/poi_count != 0:
                tmp.append((poi[i][j]/cur_sum)/(total_poi[j]/poi_count))
            else:
                tmp.append(0)
        data.append(tmp)

    # draw
    plt.figure(1)
    plt.figure(dpi=300,figsize=(24, 8))
    # plt.figure(dpi=300)
    plt.rcParams['font.family']=['SimHei']
    for i in range(cluster_num):
        ax1 = plt.subplot(2, math.ceil(cluster_num/2), 1+i)
        # ax1 = plt.subplot(math.ceil(cluster_num / 2), 2, 1 + i)
        center = data[i]
        ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
        ax1.barh(range(16), center, tick_label=[u'餐饮', u'住、宿', u'批发、零售', u'汽车销售及服务', u'金融、保险', u'教育、文化', u'卫生、社保', u'运动、休闲', u'公共设施', u'商业设施、商务服务', u'居民服务', u'公司企业', u'交通运输、仓储', u'科研及技术服务', u'农林牧渔业', u'自然地物\地名'])
        plt.title("Cluster " + str(i + 1), fontsize=18)
    plt.savefig(r'D:\aMyFile\Data\Takeout\MyData\mine\analysis\poi\grid\\grid_'+type+str(cluster_num)+'_poi_distribution.png', bbox_inches='tight')
    plt.show()

    csvFile = open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\poi\grid\\grid_"+type+str(cluster_num)+"_poi_distribution.csv",'w',newline='',encoding='utf-8-sig')
    writer = csv.writer(csvFile)
    writer.writerow([u'餐饮', u'住、宿', u'批发、零售', u'汽车销售及服务', u'金融、保险', u'教育、文化', u'卫生、社保', u'运动、休闲', u'公共设施', u'商业设施、商务服务', u'居民服务', u'公司企业', u'交通运输、仓储', u'科研及技术服务', u'农林牧渔业', u'自然地物\地名'])
    for row in data:
        writer.writerow(row)

# poi_analysis('od', 2)
# poi_analysis('od', 3)
poi_analysis('destination', 8)
# poi_analysis('destination', 3)