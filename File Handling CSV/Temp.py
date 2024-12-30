import csv

city=[]
with open(r'D:\Python code\CSV\practice_data.csv',newline='') as fp:
        s=csv.reader(fp)
        next(s)
        for rows in s:
            city.append(rows[-1])

unique_city=set(city)

print(unique_city)


