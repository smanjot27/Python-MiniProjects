import random
import datetime
def day_of_year(day,month,leap):
    dayy=0
    for i in range(1,month):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            dayy+=31
        elif i==2 and leap==True: dayy+=29
        elif i==2 and leap==False: dayy+=28
        else: dayy+=30
    dayy+=day
    return(dayy)
     
count=0
birthday=[]
while count<50:
    year=random.randint(1899,2021)
    month=random.randint(1,12)
    leap=False
    if year%4==0 and year%100!=0 or year%400==0:  leap=True 
    if month==2:
        if leap==True: day=random.randint(1,29)
        else: day=random.randint(1,28)
    else:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            day=random.randint(1,31)
        else: day=random.randint(1,30)
    dd=datetime.date(year,month,day)
    birthday.append(day_of_year(day,month,leap))
    count+=1
birthday.sort()
for i in birthday: print(i)
