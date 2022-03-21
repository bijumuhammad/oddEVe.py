import datetime


name = input("Enter the name : ")
year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
date1 = datetime.date(year, month, day)
print(name)
print(date1)

print("congratulation",name,"you will be hundred years old in",date1.year+100)