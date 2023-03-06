#Program to calculate if a given year is a leap year.
#Expression before 'or is for century years, and after 'or' is for the rest.

year = int(input('Enter year: '))
if ((year % 100 == 0) and (year % 400 == 0)) or ((year % 100 != 0) and (year % 4 == 0)):
    disekto = True
else:
    disekto = False
print(disekto)