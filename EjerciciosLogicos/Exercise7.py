year = int(input("Write the year\n"))

if(year % 4 == 0 or year % 100 == 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} isn't a leap year")
    