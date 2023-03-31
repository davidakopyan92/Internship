def check(pwd): # Correcting one mistake at a time
    if len(pwd) <= 8:
        print(f'{pwd}: Password must have more than 8 characters')
    elif '-' not in pwd:
        print(f"{pwd}: Password must contain '-' sign")
    elif pwd.isupper() or pwd.islower():
        print(f"{pwd}: Password must contain upper and lower case characters")

    else:
        print(f"{pwd}: Password set")
        return True


while not check(input('Enter a password ')): # what a Pe(a)rl :')
    continue












