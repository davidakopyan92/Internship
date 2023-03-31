def boring(n):
    i = 0
    while i < len(n)-1:
        if n[i] == n[i+1]:
            i +=1
        else:
            return False
    else:
        return True

num = input('Input at least a two-digit integer ')
print(f'is {num} boring? {boring(num)}')



