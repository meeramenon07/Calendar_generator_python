import calendar

#for monthly calendar 
year = int(input("Enter the year in numbers : "))
month = int(input(" Enter the month in numbers : "))
print(calendar.month(year,month))



#for yearly calendar
year = int(input("Enter the year in numbers : "))
print(calendar.calendar(year))
