year = int(input("Please enter year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(f"Your entered year {year}, is a leap year.")
else:
    print(f"Your entered year {year}, is not a leap year.")
