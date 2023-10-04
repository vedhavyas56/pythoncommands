import calendar
year=int(input("\n enter a year :"))
isleap=calendar.isleap(year)
if isleap:
    print("\n given year is leap year :",year)
else:
    print("\n given year is not a leap year :",year)