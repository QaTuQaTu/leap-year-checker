def is_leap_year(year):
    if x %400==0:
        return True
    elif x%100==0:
        return False
    elif x%4==0:
        return True
    else:
        return False


x=int(input('Enter the year:'))
if is_leap_year(x):
    print(x,'is leap year')
else:
    print(x,'is not leap year')
