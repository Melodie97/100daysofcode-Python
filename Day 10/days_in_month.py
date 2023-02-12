def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) == True:
        if month == 2:
            return 29
        else:
            confirmed_month = month_days[month - 1]
            return confirmed_month
    else:
        confirmed_month = month_days[month - 1]
        return confirmed_month 



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)
