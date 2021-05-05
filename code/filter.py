import csv
from itertools import islice

csv_reader = csv.reader(open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\center_deliver_OD.csv", encoding='UTF-8'))
csvFile = open(r"D:\aMyFile\Data\Takeout\MyData\mine\OD\final_data.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow(['Order ID', 'Departure Datetime', 'Departure Weekday', 'Departure lon', 'Departure lat', 'Arrival Datetime', 'Arrival Weekday', 'Arrival lon', 'Arrival lat', 'Duration', 'Distance'])

for row in islice(csv_reader, 1, None):
    if float(row[9]) > 0 and float(row[9])/60 < 90:
        if float(row[10]) > 0 and float(row[10]) < 20000:
            writer.writerow(row)

csvFile.close()

