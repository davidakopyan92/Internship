# 4564564565 random input - Lucky! :)
def luck(n):
    i = 0
    odd_sum = even_sum = 0
    while i < len(n):
        if i % 2 == 0:
            odd_sum += int(n[i])
        else:
            even_sum += int(n[i])
        i += 1
    if odd_sum == even_sum:
        return True
    else:
        return False

num = input('Try luck! Enter an integer right now! No registartion and SMS for the keybord Jedi:) ')
answer = luck(num)
print(f'Does luck even exist? {answer}')



