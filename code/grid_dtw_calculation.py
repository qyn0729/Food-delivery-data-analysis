# # import os
# #
for i in range(0, 29500, 500):
    print("nohup python -u dtw"+str(i)+".py > dtw"+str(i)+".log 2>&1 &")
#
# # #Destination
# for i in range(0, 29500, 500):
#     content = '''import collections
# import csv
# import numpy as np
# from itertools import islice
# import pandas as pd
#
# def dtw_distance(ts_a, ts_b, mww=30000):
#     """Computes dtw distance between two time series
#
#     Args:
#         ts_a: time series a
#         ts_b: time series b
#         d: distance function
#         mww: max warping window, int, optional (default = infinity)
#
#     Returns:
#         dtw distance
#     """
#
#     # Create cost matrix via broadcasting with large int
#     d = lambda x, y: abs(x - y)
#     # d = lambda x, y: math.sqrt(x*x + y*y)
#     ts_a, ts_b = np.array(ts_a), np.array(ts_b)
#     M, N = len(ts_a), len(ts_b)
#     cost = np.ones((M, N))
#
#     # Initialize the first row and column
#     cost[0, 0] = d(ts_a[0], ts_b[0])
#     for i in range(1, M):
#         cost[i, 0] = cost[i - 1, 0] + d(ts_a[i], ts_b[0])
#
#     for j in range(1, N):
#         cost[0, j] = cost[0, j - 1] + d(ts_a[0], ts_b[j])
#
#     # Populate rest of cost matrix within window
#     for i in range(1, M):
#         for j in range(max(1, i - mww), min(N, i + mww)):
#             choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
#             cost[i, j] = min(choices) + d(ts_a[i], ts_b[j])
#
#     # Return DTW distance given window
#     return cost[-1, -1]
#
# csv_reader = csv.reader(open("normalized_destination_count.csv", encoding='UTF-8'))
#
# X = []
# for row in islice(csv_reader, 2, None):
#     tmp = []
#     for i in range(2, len(row)):
#         tmp.append(float(row[i]))
#     X.append(tmp)
#
# roadnet_num = len(X)
# print(roadnet_num)
# finish_dtw_value = np.zeros((1000, roadnet_num))
# finishdtw = open(r"temp_finish'''+str(i)+'''.csv","w", encoding='UTF-8', newline='')
# finish_writer = csv.writer(finishdtw)
# '''+"i="+str(i)+'''
# start='''+str(i)+'''
# while i < start+500 and i < roadnet_num:
#     print(i)
#     j = i + 1
#     while j < roadnet_num:
#         finish11 = X[i][:6]
#         finish12 = X[i][6:12]
#         finish13 = X[i][12:18]
#         finish14 = X[i][18:24]
#         finish15 = X[i][24:30]
#         finish16 = X[i][30:36]
#         finish17 = X[i][36:42]
#         finish18 = X[i][42:48]
#         finish19 = X[i][48:54]
#         finish110 = X[i][54:60]
#         finish111 = X[i][60:66]
#         finish112 = X[i][66:72]
#
#         finish21 = X[j][:6]
#         finish22 = X[j][6:12]
#         finish23 = X[j][12:18]
#         finish24 = X[j][18:24]
#         finish25 = X[j][24:30]
#         finish26 = X[j][30:36]
#         finish27 = X[j][36:42]
#         finish28 = X[j][42:48]
#         finish29 = X[j][48:54]
#         finish210 = X[j][54:60]
#         finish211 = X[j][60:66]
#         finish212 = X[j][66:72]
#         finish_dtw_value[i-start][j] = dtw_distance(finish11, finish21) + dtw_distance(finish12, finish22) + dtw_distance(finish13, finish23) + dtw_distance(finish14, finish24) + dtw_distance(finish15, finish25) + dtw_distance(finish16, finish26) + dtw_distance(finish17, finish27) + dtw_distance(finish18, finish28) + dtw_distance(finish19, finish29) + dtw_distance(finish110, finish210) + dtw_distance(finish111, finish211) + dtw_distance(finish112, finish212)
#         j = j + 1
#     finish_writer.writerow(finish_dtw_value[i-start])
#     print(finish_dtw_value[i-start])
#     i = i + 1
# '''
#     filename = "dtw"+str(i)
#     f = open('D:\\aMyFile\\毕设\\program\\dtw\\destination\\'+filename+'.py', "w")
#     f.write(content)
#     f.close()
#     print(i)
# # #
# #
# #
# # # ------------------------------
# # #od
# # for i in range(0, 29500, 500):
# #     content = '''import collections
# # import csv
# # import numpy as np
# # from itertools import islice
# # import pandas as pd
# #
# # def dtw_distance(ts_a, ts_b, mww=30000):
# #     """Computes dtw distance between two time series
# #
# #     Args:
# #         ts_a: time series a
# #         ts_b: time series b
# #         d: distance function
# #         mww: max warping window, int, optional (default = infinity)
# #
# #     Returns:
# #         dtw distance
# #     """
# #
# #     # Create cost matrix via broadcasting with large int
# #     d = lambda x, y: abs(x - y)
# #     # d = lambda x, y: math.sqrt(x*x + y*y)
# #     ts_a, ts_b = np.array(ts_a), np.array(ts_b)
# #     M, N = len(ts_a), len(ts_b)
# #     cost = np.ones((M, N))
# #
# #     # Initialize the first row and column
# #     cost[0, 0] = d(ts_a[0], ts_b[0])
# #     for i in range(1, M):
# #         cost[i, 0] = cost[i - 1, 0] + d(ts_a[i], ts_b[0])
# #
# #     for j in range(1, N):
# #         cost[0, j] = cost[0, j - 1] + d(ts_a[0], ts_b[j])
# #
# #     # Populate rest of cost matrix within window
# #     for i in range(1, M):
# #         for j in range(max(1, i - mww), min(N, i + mww)):
# #             choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
# #             cost[i, j] = min(choices) + d(ts_a[i], ts_b[j])
# #
# #     # Return DTW distance given window
# #     return cost[-1, -1]
# #
# # csv_reader = csv.reader(open("normalized_od_count.csv", encoding='UTF-8'))
# #
# # X = []
# # for row in islice(csv_reader, 2, None):
# #     tmp = []
# #     for i in range(2, len(row)):
# #         tmp.append(float(row[i]))
# #     X.append(tmp)
# #
# # roadnet_num = len(X)
# # print(roadnet_num)
# # origin_dtw_value = np.zeros((1000, roadnet_num))
# # finish_dtw_value = np.zeros((1000, roadnet_num))
# # full_dtw_value = np.zeros((roadnet_num, roadnet_num))
# # '''+'''origindtw = open(r"temp_origin'''+str(i)+'''.csv","w", encoding='UTF-8', newline='')'''+'''
# # origin_writer = csv.writer(origindtw)
# # finishdtw = open(r"temp_finish'''+str(i)+'''.csv","w", encoding='UTF-8', newline='')
# # finish_writer = csv.writer(finishdtw)
# # '''+'''fulldtw = open(r"temp_full'''+str(i)+'''.csv","w", encoding='UTF-8', newline='')'''+'''
# # full_writer = csv.writer(fulldtw)
# # '''+"i="+str(i)+'''
# # start='''+str(i)+'''
# # while i < start+500 and i < roadnet_num:
# #     print(i)
# #     j = i + 1
# #     while j < roadnet_num:
# #         origin11 = X[i][:6]
# #         origin12 = X[i][6:12]
# #         origin13 = X[i][12:18]
# #         origin14 = X[i][18:24]
# #         origin15 = X[i][24:30]
# #         origin16 = X[i][30:36]
# #         origin17 = X[i][36:42]
# #         origin18 = X[i][42:48]
# #         origin19 = X[i][48:54]
# #         origin110 = X[i][54:60]
# #         origin111 = X[i][60:66]
# #         origin112 = X[i][66:72]
# #         finish11 = X[i][72:78]
# #         finish12 = X[i][78:84]
# #         finish13 = X[i][84:90]
# #         finish14 = X[i][90:96]
# #         finish15 = X[i][96:102]
# #         finish16 = X[i][102:108]
# #         finish17 = X[i][108:114]
# #         finish18 = X[i][114:120]
# #         finish19 = X[i][120:126]
# #         finish110 = X[i][126:132]
# #         finish111 = X[i][132:138]
# #         finish112 = X[i][138:144]
# #
# #         origin21 = X[j][:6]
# #         origin22 = X[j][6:12]
# #         origin23 = X[j][12:18]
# #         origin24 = X[j][18:24]
# #         origin25 = X[j][24:30]
# #         origin26 = X[j][30:36]
# #         origin27 = X[j][36:42]
# #         origin28 = X[j][42:48]
# #         origin29 = X[j][48:54]
# #         origin210 = X[j][54:60]
# #         origin211 = X[j][60:66]
# #         origin212 = X[j][66:72]
# #         finish21 = X[j][72:78]
# #         finish22 = X[j][78:84]
# #         finish23 = X[j][84:90]
# #         finish24 = X[j][90:96]
# #         finish25 = X[j][96:102]
# #         finish26 = X[j][102:108]
# #         finish27 = X[j][108:114]
# #         finish28 = X[j][114:120]
# #         finish29 = X[j][120:126]
# #         finish210 = X[j][126:132]
# #         finish211 = X[j][132:138]
# #         finish212 = X[j][138:144]
# #         origin_dtw_value[i-start][j] = dtw_distance(origin11, origin21) + dtw_distance(origin12, origin22) + dtw_distance(origin13, origin23) + dtw_distance(origin14, origin24) + dtw_distance(origin15, origin25) + dtw_distance(origin16, origin26) + dtw_distance(origin17, origin27) + dtw_distance(origin18, origin28) + dtw_distance(origin19, origin29) + dtw_distance(origin110, origin210) + dtw_distance(origin111, origin211) + dtw_distance(origin112, origin212)
# #         finish_dtw_value[i-start][j] = dtw_distance(finish11, finish21) + dtw_distance(finish12, finish22) + dtw_distance(finish13, finish23) + dtw_distance(finish14, finish24) + dtw_distance(finish15, finish25) + dtw_distance(finish16, finish26) + dtw_distance(finish17, finish27) + dtw_distance(finish18, finish28) + dtw_distance(finish19, finish29) + dtw_distance(finish110, finish210) + dtw_distance(finish111, finish211) + dtw_distance(finish112, finish212)
# #         full_dtw_value[i-start][j] = origin_dtw_value[i-start][j]+finish_dtw_value[i-start][j]
# #         j = j + 1
# #     full_writer.writerow(full_dtw_value[i-start])
# #     print(full_dtw_value[i-start])
# #     i = i + 1
# # '''
# #     filename = "dtw"+str(i)
# #     f = open('D:\\aMyFile\\毕设\\program\\dtw\\od\\'+filename+'.py', "w")
# #     f.write(content)
# #     f.close()
# #     print(i)