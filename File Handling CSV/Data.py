import csv
all_data=[]
with open(r'D:\Python code\CSV\practice_data.csv', newline='') as fp:
    s = csv.reader(fp)
    next(s)
    for all in s:
        all_data.append(all)

    print(all_data)


