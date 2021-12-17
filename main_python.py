from datetime import date
from dateutil.relativedelta import relativedelta

print("Enter the first date")
fd_year = int(input("Enter a year: "))
fd_month = int(input("Enter a month: "))
fd_day = int(input("Enter a day: "))

print("\nEnter the second date")
sd_year = int(input("Enter a year: "))
sd_month = int(input("Enter a month: "))
sd_day = int(input("Enter a day: "))

try:
    fd = date(fd_year, fd_month, fd_day)
    sd = date(sd_year, sd_month, sd_day)
    
    difference = sd - fd
    print(f"\n{difference} days have passed already")

    #let's convert days into months and years
    
    diff_months = relativedelta(sd, fd)
    print ("\nAge in years - ", diff_months.years)
    print ("Age in months - ", diff_months.months)
    print ("Age in days - ", diff_months.days)
    
except ValueError:
    print("\n\nWrong date!")
    
# except ValueError: invalid literal for int() with base 10:
#     print("\n\nInput date!")
