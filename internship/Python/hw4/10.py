# probability of bein equal is lower, so I place it at the end of the conditional statement
def my_max(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'equal'

print(my_max(-0.5, 1.05))
