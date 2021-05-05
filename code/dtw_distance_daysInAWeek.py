import csv
import matplotlib.pyplot as plt
from itertools import islice
from collections import Counter
import datetime
import numpy as np

def dtw_distance(ts_a, ts_b, mww=10000):
    """Computes dtw distance between two time series

    Args:
        ts_a: time series a
        ts_b: time series b
        d: distance function
        mww: max warping window, int, optional (default = infinity)

    Returns:
        dtw distance
    """

    # Create cost matrix via broadcasting with large int
    d = lambda x, y: abs(x - y)
    # d = lambda x, y: math.sqrt(x*x + y*y)
    ts_a, ts_b = np.array(ts_a), np.array(ts_b)
    M, N = len(ts_a), len(ts_b)
    cost = np.ones((M, N))

    # Initialize the first row and column
    cost[0, 0] = d(ts_a[0], ts_b[0])
    for i in range(1, M):
        cost[i, 0] = cost[i - 1, 0] + d(ts_a[i], ts_b[0])

    for j in range(1, N):
        cost[0, j] = cost[0, j - 1] + d(ts_a[0], ts_b[j])

    # Populate rest of cost matrix within window
    for i in range(1, M):
        for j in range(max(1, i - mww), min(N, i + mww)):
            choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
            cost[i, j] = min(choices) + d(ts_a[i], ts_b[j])

    # Return DTW distance given window
    return cost[-1, -1]

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\origin_final_data.csv", encoding='UTF-8'))
week_count = [0]*8
exist_days = {}
week_hours = [0]*8
for i in range(len(week_hours)):
    week_hours[i] = [0]*24

for row in islice(csv_reader, 1, None):
    week = int(row[2])
    dateTime = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    hour = int(dateTime.strftime(('%H')))
    date = dateTime.date()
    if not exist_days.__contains__(date):
        exist_days[date] = 1
        week_count[week] += 1
    week_hours[week][hour] += 1
print(week_count)

value = 100000000
minval = [value]*8
value = -1
maxval = [value]*8

for i in range(1, 8):
    for j in range(24):
        week_hours[i][j] = week_hours[i][j] / week_count[i]
        if week_hours[i][j] < minval[i]:
            minval[i] = week_hours[i][j]
        if week_hours[i][j] > maxval[i]:
            maxval[i] = week_hours[i][j]

# normalization
for i in range(1, len(week_hours)):
    for j in range(len(week_hours[i])):
        if maxval[i] - minval[i] != 0:
            week_hours[i][j] = (week_hours[i][j]-minval[i]) / (maxval[i] - minval[i])

#draw picture
hour = np.array(range(24))
plt.figure(1)

for i in range(1, 8):
    p = 240+i
    ax1 = plt.subplot(p)
    plt.ylim(0, 1)
    plt.xlabel('Time')
    plt.ylabel('Order Counts')
    plt.xticks([0, 6, 12, 18, 24])
    data = week_hours[i]
    ax1.plot(hour, data, color="g")
plt.savefig(r'D:\aMyFile\Data\Takeout\MyData\mine\statistics\dtw_distance_inweek_origin.png')
plt.show()

#calculate dtw distance
csvFile = open(r"D:\aMyFile\Data\Takeout\MyData\mine\statistics\dtw_distance_inweek_origin.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
dtw = [0]*8
for i in range(len(dtw)):
    dtw[i] = [0]*8
for i in range(1, 8):
    for j in range(i+1, 8):
        dtw[i][j] = dtw_distance(week_hours[i], week_hours[j])
        dtw[j][i] = dtw[i][j]
    writer.writerow(dtw[i][1:])
