year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(str(year) + ' is leap year.')
        else:
            print(str(year) + ' is not a leap year.')
    else:
        print(str(year) + ' is a leap year.')
else:
    print(str(year) + ' is not a leap year.')