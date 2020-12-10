# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or # returns None if any of the arguments is invalid.

def isYearLeap(year):
    if year%100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else: 
        return False

def daysInMonth(year, month):
    if month > 7:
        if month % 2 == 0:
            return 31
        else:
            return 30

    else:
        if month % 2 == 0:
            if month == 2:
                if isYearLeap(year):
                    return 29
                else:
                    return 28
            else:
                return 30
        else:
            return 31
                    
        

def dayOfYear(year, month, day):
    days = day
    for i in range(1, month):
        days = days + daysInMonth(year, i)
    
    return days

print("This program will tell you the day of the year any date is.")

yy = int((input("Year: ")))
mm = int((input("Month: ")))
dd = int((input("Day: ")))

print(dayOfYear(yy, mm, dd))
