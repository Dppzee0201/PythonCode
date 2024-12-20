import csv
# with open(r"D:\Python code\CSV\Random.csv",'w') as fp:
#     s=csv.writer(fp)
#     s.writerow(['Id', 'Name', 'City'])
#     s.writerows([[1,'Name1','Pune'],[2,'Name2','Mumbai'],[3,'Name3','Pune'],[4,'Name4','Mumbai'],[5,'Name5','Pune'],[6,'Name6','Pune']])

import csv

with open(r"D:\Python code\CSV\Random.csv", newline='') as fp:
    s = csv.reader(fp)
    for row in s:
      #  if row:  # Skip empty rows
            print(row)













