### only slow sorting ###
def slow_sort_again(lst, param):
    i = 0
    j = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if param == 'asc':
                if lst[i] < lst[j]:
                    lst[j], lst[i] = lst[i], lst[j]
            elif param == 'dsc':
                if lst[i] > lst[j]:
                    lst[j], lst[i] = lst[i], lst[j]
    print(lst)

### Version II ### which I prefer
def slow_sort(loc):
    for item_index in range(len(loc)):
        for run_index in range(len(loc)):
            if loc[item_index] > loc[run_index]:
                if run_index < item_index:  # > for descending;
                    continue
                loc[run_index], loc[item_index] = loc[item_index], loc[run_index]
    print(loc)


# these test lists are quite good in my Humble opinion.
l1 = [4, 0, 1, 0.5, -7, 255, 3]
l2 = [-3, 77, 11, 0, -2, 5, 10]
l3 = [5, 2, 3, 1, 0]
l4 = ['Yerevan', 'Moon', 'Mars', 'Florida', 'Past']

slow_sort_again(l1, 'asc')
slow_sort_again(l2, 'dsc')
slow_sort_again(l4, 'asc')

print('Version II, ascending:')
slow_sort(l1)
slow_sort(l4)



