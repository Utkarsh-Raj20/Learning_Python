def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))