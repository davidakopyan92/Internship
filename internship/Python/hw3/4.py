print(' *** Welcome to doggo age converter xD ***')
print('    Scientific accuracy is not pursued')
years = int(input("Enter dog's full human years "))
months = int(input("Enter dog's full human months "))
days = int(input("Enter dog's human days "))

if years <= 2:
    year_equiv = 10.5
    mon2year_equiv = 10.5 / 24
    day2year_equiv = 10.5 / 365

    age = round(years * year_equiv + months * mon2year_equiv + days * day2year_equiv)
    print(f"Doggo's {age} human years")
else:
    year_equiv = 4
    mon2year_equiv = 4 / 12
    day2year_equiv = 4 / 365

    age = round(2 * 10.5 + (years - 2 ) * year_equiv + months * mon2year_equiv + days * day2year_equiv)
    print(f"Doggo's {age} human years")
