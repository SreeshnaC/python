year=int(input("enter a year to check leap year or not:"))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"is leap year")
else:
    print(year, "is not leap year" )