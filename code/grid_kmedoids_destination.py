import numpy as np
import csv
from sklearn_extra.cluster import KMedoids
import tslearn.metrics as metrics
from tslearn.clustering import silhouette_score
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from tslearn.generators import random_walks
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from itertools import islice
import math
import matplotlib.ticker as mtick
from matplotlib.collections import LineCollection


# elbow法则找最佳聚类数，结果：elbow = 5
def test_elbow(X, dtw_value, seed):
    print(len(X))
    distortions = []
    silhouette_value = []
    dists = dtw_value
    print(dists)
    if seed == -1:
        for seed in range(0, 21):
            cur_silhouette = [seed]
            cur_distortions = [seed]
            for i in range(2, 15):
                print(i)
                km = KMedoids(n_clusters=i, random_state=seed, metric="precomputed", init='k-medoids++', max_iter=30000)
                km.fit(dists)
                # 记录误差和
                cur_distortions.append(km.inertia_)
                y_pred = km.fit_predict(dists)
                np.fill_diagonal(dists, 0)
                score = silhouette_score(dists, y_pred, metric="precomputed")
                cur_silhouette.append(score)
            distortions.append(cur_distortions)
            silhouette_value.append(cur_silhouette)
        with open(r".//res//grid_distortions_destination.csv", "w",encoding='UTF-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in distortions:
                writer.writerow(row)
                print(row)
        with open(r".//res//grid_silhouette_destination.csv", "w",encoding='UTF-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in silhouette_value:
                writer.writerow(row)
                print(row)
    else:
        csv_reader = csv.reader(open(".//res//grid_distortions_destination.csv", encoding='UTF-8'))
        for row in csv_reader:
            distortions.append([float(item) for item in row])
        csv_reader = csv.reader(open(".//res//grid_silhouette_destination.csv", encoding='UTF-8'))
        for row in csv_reader:
            silhouette_value.append([float(item) for item in row])
        chosen_distortions = distortions[seed][1:]
        chosen_silhouette = silhouette_value[seed][1:]
        plt.figure(1)
        plt.plot(range(2, 15), chosen_distortions, marker='o')
        plt.xlabel('Number of clusters')
        plt.ylabel('Distortion')
        plt.savefig(r'.//res//grid_distortions_destination.png')
        plt.close()
        plt.figure(1)
        plt.bar(range(2, 15), chosen_silhouette, color='grey')
        plt.xlabel('Number of clusters')
        plt.ylabel('Silhouette score')
        plt.savefig(r'.//res//grid_silhouette_destination.png')


def test_kmedoids(dtw_value, cluster_num, seed):
    # 声明precomputed自定义相似度计算方法
    km = KMedoids(n_clusters=cluster_num, random_state=seed, metric="precomputed", init='k-medoids++', max_iter=30000)
    dists = dtw_value
    y_pred = km.fit_predict(dists)
    with open(r".//res//grid_pred_d"+str(cluster_num)+".csv", "w", encoding='UTF-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        index = 0
        for row in y_pred:
            writer.writerow([row])
            index += 1
    with open(r".//res//grid_centroids_d"+str(cluster_num)+".csv", "w", encoding='UTF-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for yi in range(cluster_num):
            writer.writerow([km.medoid_indices_[yi]])
    print('finish')


def kmedoids(func, cluster_num, seed):
    X = []
    for i in range(0, 29500, 500):
        csv_reader = csv.reader(open("temp_finish" + str(i) + ".csv", encoding='UTF-8'))
        for row in csv_reader:
            X.append(row)
    roadnet_num = len(X)
    dtw_value = np.zeros((roadnet_num, roadnet_num), dtype='float32')
    for i in range(len(X)):
        for j in range(len(X[i])):
            if j > i:
                dtw_value[i][j] = X[i][j]
            else:
                dtw_value[i][j] = X[j][i]

    if func == 1:
        test_elbow(X, dtw_value, seed)
    else:
        test_kmedoids(dtw_value, cluster_num, seed)


def draw_result(cluster_num, normalized):
    classes = {}
    class_cnt = [0] * cluster_num
    dict = {}
    ave_weekday = {}
    ave_sat = {}
    ave_sun = {}

    for i in range(cluster_num):
        ave_weekday[i] = [0] * 24
        ave_sat[i] = [0] * 24
        ave_sun[i] = [0] * 24

    index = 0
    csv_reader = csv.reader(
        open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_centroids_d" +str(cluster_num) + ".csv"))
    for row in csv_reader:
        dict[int(row[0])] = index
        index += 1

    index = 0
    csv_reader = csv.reader(
        open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_d" + str(cluster_num) + ".csv"))
    for row in csv_reader:
        classes[index] = int(row[0])
        class_cnt[int(row[0])] += 1
        index += 1
    print(index)


    if normalized == 0:
        csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\destination_count.csv"))
    else:
        csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\normalized_destination_count.csv"))
    index = 0
    series = {}
    data = {}
    for row in islice(csv_reader, 2, None):
        cur_class = classes[index]
        cur_data = [float(item) for item in row[2:]]
        for i in range(24):
            ave_weekday[cur_class][i] += cur_data[i] / class_cnt[cur_class]
        for i in range(24):
            ave_sat[cur_class][i] += cur_data[i + 24] / class_cnt[cur_class]
        for i in range(24):
            ave_sun[cur_class][i] += cur_data[i + 48] / class_cnt[cur_class]
        index += 1

    if normalized == 1:
        with open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_d" + str(cluster_num) + "_normalized_ave.csv", "w", encoding='UTF-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(24):
                row = []
                for j in range(cluster_num):
                    row.append(ave_weekday[j][i])
                    row.append(ave_sat[j][i])
                    row.append(ave_sun[j][i])
                writer.writerow(row)
    else:
        with open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_d" + str(cluster_num) + "_ave.csv", "w", encoding='UTF-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(24):
                row = []
                for j in range(cluster_num):
                    row.append(ave_weekday[j][i])
                    row.append(ave_sat[j][i])
                    row.append(ave_sun[j][i])
                writer.writerow(row)


    # hour = np.array(range(24))
    # plt.figure(1)
    # # plt.figure(dpi=300, figsize=(24, 8))
    # plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    #
    # for i in range(cluster_num):
    #     ax1 = plt.subplot(2, math.ceil(cluster_num / 2), 1 + i)
    #     ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
    #     plt.xticks([0, 6, 12, 18, 23])
    #     ax1.set_xticklabels(['0:00\nOrder Finish Time', '6:00', '12:00', '18:00', '23:00'], rotation=0)
    #     ax1.set_ylabel('Order Count')
    #     ax1.plot(hour, ave_weekday[i], "blue", label='Weekdays')
    #     ax1.plot(hour, ave_sat[i], "#f48b29", label='Saturday')
    #     ax1.plot(hour, ave_sun[i], "#f0c929", label='Sunday')
    #     ax1.legend()
    #     plt.grid(linestyle='--')
    #     plt.title("Cluster " + str(i + 1), fontsize=18)
    #     if normalized == 1:
    #         plt.ylim(0, 1)
    # if normalized == 0:
    #     plt.savefig(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_d" + str(cluster_num) + "_ave.png",bbox_inches='tight')
    # else:
    #     plt.savefig(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_d" + str(
    #         cluster_num) + "_normalized_ave.png", box_inches='tight')
    # plt.show()


# def kmedoids(func, cluster_num, seed)
# ----------------------
# kmedoids(1, 3, 18)
# kmedoids(2, 2, 18)
# kmedoids(2, 3, 18)

# def draw_result(cluster_num, normalized):
# ----------------------
draw_result(2, 0)
draw_result(2, 1)
# draw_result(8, 0)
# draw_result(8, 1)