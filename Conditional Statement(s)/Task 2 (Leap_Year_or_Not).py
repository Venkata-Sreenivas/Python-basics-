''' Accept year from the user findout the given year is leap year or not'''

import calendar

#Conditional  Statement
year=int(input("Enter year: "))

if calendar.isleap(year):
    print("Leap Year")
else:
    print("Not Leap Year")

#Conditional Operator
print("Leap Year") if calendar.isleap(year) else print("Not Leap Year")
