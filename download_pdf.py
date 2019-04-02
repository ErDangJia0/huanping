import csv
import requests

csvFile = open('huanping.csv', 'r')
reader = csv.reader(csvFile)
for item in reader:
    if reader.line_num == 1:
        continue
    filename = item[3] + "环境影响报告.pdf"
    res = requests.get(item[5])
    data = res.content
    with open(filename, 'wb') as f:
        f.write(data)
        print(filename+'已经完成')
