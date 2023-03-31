i = 0
fib = num = 1
prev = 0
while i <= 47:
    prev = num
    num = fib
    fib = prev + num
    print(fib)
    i += 1


