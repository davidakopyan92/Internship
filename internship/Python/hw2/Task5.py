even_list = []
for i in range(10):
    if i % 2 == 0:
        even_list.append(i)
unpacked = ''
for j in even_list:
    unpacked += str(j) + ' '
print('These are even numbers:', unpacked)  # I could go ",main_list", but it would be printed as a list with []

copy_list = even_list.copy()
total = 0
for x in copy_list:
    total += x
    avg = total / len(copy_list)
print('average is:', avg)

removed = copy_list.pop(2)
print('popped value:', removed)

# list of 5 odd numbers...
odd_list =[]
for i in range(10):
    if i % 2 != 0:
        odd_list.append(i)
mutant_list = even_list + odd_list
mutant_list.sort()
print(mutant_list)


