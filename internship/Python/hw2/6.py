list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
#list2 = [5, 4, 3, 2, 1]


def cshift(lst1, lst2):
    i = 0
    j = len(list2)-1

    for x in lst1:
        if lst1[i] == lst2[j]:
            i += 1
            j -= 1
    else:
        print('Lists are not cyclic shifts')
    if j < 0:
        print('Lists are cyclic shifts')

cshift(list1, list2)
