import math

date = input("input date and number of days (DDMMYY K)")
day = int(date[0:2])
month = int(date[2:4])
year = int(date[4:6])
k = int(date[7: len(date)+1])
"""
y=k/360
year =year + y
d=k % 360"""
k2 = k
for i in range(k2):
    if day == 30:
        
        if month == 12:
            year = year + 1
            month = 1
        else:
            month=month+1
        day = 0
        k=k-1
    else:
        day=day+1
        k=k-1
    

print(day, month, year)
    
