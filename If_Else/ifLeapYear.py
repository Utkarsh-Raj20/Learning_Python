def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
    return leap

year = int(input("year: "))
if is_leap(year) == True:
    print("This is a leap Year")
else:
    print("This is not a leap Year")