year=int(input("enter any year : "))  
if(year%400==0) or (year%4==0 and year% 100!=0):
    print("\n given year is a leap year : ", year)
else:
    print("\n given year is not a leap year : ",year)