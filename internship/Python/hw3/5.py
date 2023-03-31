decision = input('Enter 1 for C --> F conversion or 2 for F --> C ')
degree = float(input('Enter a degree '))

# c/5 = f/9 -32/9
if decision == '1':
    f = round((9 * degree + 160) / 5)
    print(f'{degree} Celsius is {f} in Fahrenheit')
if decision == '2':
    c = round((5 * degree - 160) / 9)
    print(f'{degree} Fahrenheit is {c} in Celsius')