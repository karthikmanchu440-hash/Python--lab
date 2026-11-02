year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year}is Leap year")
elif year % 100 == 0:
    print(f"{year}is Not a leap year")
elif year % 4 == 0:
    print(f"{year}is Leap year")
else:
    print(f"{year}is Not a leap year")
