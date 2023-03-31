# There are numerous test cases to fail with this code, but I am not even trying to cover them.
# I am sure it is not expected with the task like this.
string = input('Input anything ')
print(f'Input string is: {string}')

list = string.split(' ')
list2 = []
for x in list:
    list2.append(x.capitalize())
result = ' '.join(list2)
print(f'Result is: {result}')
