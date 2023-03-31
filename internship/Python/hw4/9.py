def space_remover(lst):
    lst = lst.split()
    lst = ' '.join(lst)
    return lst.split()

def average(data):
    ave = sum(data) / len(data)
    return ave


xlist = input('Enter x coordinates separated with spaces ')
ylist = input('Enter y coordinates separated with spaces ')

xlist = space_remover(xlist)
xlist = [float(x) for x in xlist]
ylist = space_remover(ylist)
ylist = [float(y) for y in ylist]

print(xlist, ylist)
aver_x = average(xlist)
aver_y = average(ylist)

### Calculation of m taking into consideration floating point limitations ###
sum_xy = 0
sum_sqx = 0
sq_sumx = 0
i = 0

while i < len(xlist) and i < len(ylist):
    sum_xy += (xlist[i] * ylist[i])
    sum_sqx += (xlist[i] * xlist[i])
    i += 1
sum_xy = round(sum_xy,2)
sq_sumx = round(sum(xlist) * sum(xlist), 2)

print(f'sum_xy = {sum_xy}, sum_sqx = {sum_sqx}, sq_sumx = {sq_sumx}, aver_x = {aver_x}, aver_y= {aver_y}')
m = (sum_xy - sum(xlist) * sum(ylist) / len(xlist)) / (sum_sqx - sq_sumx/len(xlist))
m = round(m,2)
print('m =',m)
b = round((aver_y - m * aver_x),1)
print('b =', b)

print(f'\ny = {m}x+{b}')
