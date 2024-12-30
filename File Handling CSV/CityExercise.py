import csv
with open(r'D:\Python code\CSV\practice_data.csv') as fp:
    s=csv.reader(fp)
    for rows in s:
        city=rows[-1]
        print(city)




