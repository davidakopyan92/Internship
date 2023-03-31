# it is impossible to predict whether sequence reaches 1 for any integer, so I put a limitation of operations
def wonder(n):
    sequence = ''
    limit = 0
    while n != 1 and limit < 100:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1

        sequence += ' ' + str(n)
        limit += 1
    return sequence

num = int(input('Input a number'))
print(wonder(num))