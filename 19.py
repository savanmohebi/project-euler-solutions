def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

days_in_month = [31, 28, 31, 30, 31, 30, 
                 31, 31, 30, 31, 30, 31]

weekday = 0  
sundays_count = 0

for year in range(1900, 2001):
    for month in range(12):
       
        if year >= 1901 and weekday == 6:
            sundays_count += 1
        
        days = days_in_month[month]
        if month == 1 and isleap(year):
            days += 1 
        
        weekday = (weekday + days) % 7

print(sundays_count)
