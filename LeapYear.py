# To find year is leap year or not.
year = int(input("Enter the year:"))
if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
    print("Year is Leap year!")
else:
    print("Year is not leap year")
