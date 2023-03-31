myList = [[1,2,3,4,5],[6,7,8,9],[10,11,12]]

def func(lst):
    return lst[1][1], lst[1][2]

def func2(lst):
    return lst[0][-2:], lst[1][:2]

def rev(lst):
    i = 0
    newlist = []
    j=0
    for x in lst:
        i = len(x)-1
        newlist.append([])
        while i >= 0:
            newlist[j].append(x[i])
            i -= 1
        j += 1
    print('Sublists items order reversed:',newlist)

    rev_list = []
    for x in newlist:
        rev_list.insert(0, x)
    print('and now sublists order is reversed as well:', rev_list)

myList2 = []
i=-1
for x in myList[0]:
    while i > -4:
        myList2.append(myList[0][i])
        i -=1
myList2.append(myList[1][3])
myList2.append(myList[2][0])
print('Created with a bit of auto:', myList2)

rev(myList)
print('returned:', list(func(myList)))
print('returned:', list(func2(myList)))










