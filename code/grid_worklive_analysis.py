import csv
from itertools import islice

work_class = [1]
live_class = [0]
work_cnt = 0
live_cnt = 0
commerce_cnt = 0

classes = {}

# weekday 11:00-13:00
work_weekday_noon = {}
# weekday 20:00-24:00
work_weekday_extrawork = {}
# sat&sun 11:00-13:00, 17:00-20:00
work_sat = {}
work_sun = {}
# sat&sun 11:00-13:00, 17:00-20:00
live_weekend = {}
# weekday 22:00-24:00
live_weekday_supper = {}
# sat&sun 22:00-24:00
live_weekend_supper = {}


index = 0
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\kmedoids\grid\grid_pred_d2.csv"))
for row in csv_reader:
    classes[index] = int(row[0])
    index += 1

index = 0
csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\destination_count.csv"))
for row in islice(csv_reader, 2, None):
    cur_class = classes[index]
    x = float(row[0])
    y = float(row[1])
    cur_data = [float(item) for item in row[2:]]
    if work_class.__contains__(cur_class):
        work_weekday_noon[str(x) + '-' + str(y)] = sum(cur_data[11:13]) / 2
        work_weekday_extrawork[str(x) + '-' + str(y)] = sum(cur_data[20:24]) / 4
        work_sat[str(x) + '-' + str(y)] = (sum(cur_data[35:37])+sum(cur_data[41:44])) / 5
        work_sun[str(x) + '-' + str(y)] = (sum(cur_data[59:61])+sum(cur_data[65:68])) / 5
    if live_class.__contains__(cur_class):
        live_weekend[str(x) + '-' + str(y)] = (sum(cur_data[59:61])+sum(cur_data[65:68])+sum(cur_data[59:61])+sum(cur_data[65:68])) / 10
        live_weekday_supper[str(x) + '-' + str(y)] = sum(cur_data[22:24]) / 2
        live_weekend_supper[str(x) + '-' + str(y)] = (sum(cur_data[46:48])+sum(cur_data[70:72])) / 4
    index += 1

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\work_live\workplace_order_cnt_d2.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'work_weekday_noon', 'work_weekday_extrawork', 'work_sat', 'work_sun'])
    for item in work_weekday_noon:
        row = [item.split('-')[0], item.split('-')[1], work_weekday_noon[item], work_weekday_extrawork[item], work_sat[item], work_sun[item]]
        writer.writerow(row)

with open(r"D:\aMyFile\Data\Takeout\MyData\mine\analysis\work_live\liveplace_order_cnt_d2.csv","w", encoding='UTF-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'live_weekend', 'live_weekday_supper', 'live_weekend_supper'])
    for item in live_weekend:
        row = [item.split('-')[0], item.split('-')[1], live_weekend[item], live_weekday_supper[item], live_weekend_supper[item]]
        writer.writerow(row)


