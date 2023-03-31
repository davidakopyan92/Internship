numbers = []
for x in range(3):
    numbers.append(float(input('input a number ')))
    print(f'Number {x} is : ', numbers[x])
# I could let the user input numbers at once and other stuff, but
# this is not what the problem is about.
numbers.sort()
median = numbers[1] # having only 3 numbers lets me do this
print('Median is:', median)

