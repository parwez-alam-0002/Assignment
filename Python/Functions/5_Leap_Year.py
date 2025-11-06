# check the year is leap year or not
def Check_Leap_Year(year)->str:
    if year % 4 ==0 and year % 100 !=0:
        return "Leap Year"
    elif year % 400==0:
        return "Leap Year"
    else:
        return "Not a Leap Year"


year=int(input("Enter a year : "))
print(Check_Leap_Year(year))
