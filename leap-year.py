year = int(input("Enter the year to check if it is a leap year\n"))
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0 :
    print(year, "is a leap year")
else :
    print(year, "isn't a leap year")
