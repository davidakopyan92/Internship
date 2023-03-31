nationality = {'Armenian': 'Բարև', 'Russian, Georgian': 'Добрый день'}
answer = input('Please enter your nationality ')

for i in nationality:
    key_list = i.split(', ') # I use this to prevent greetings other than "Hello" for nationalities like "Ar", "ian"... etc.
    if answer in key_list:
        print(nationality[i])
        break
else:
    print('Hello!')















