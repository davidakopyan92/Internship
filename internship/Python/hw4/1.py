def isperfect(n):
    i = n-1
    total = 0
    while i >= 1:
        if n % i == 0:
            total += i
        i -= 1
    if total == n:
        return True


num = 10001
for x in range(1, num):
    if isperfect(x):
        print(x)

