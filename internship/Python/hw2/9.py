phrase = input('Input something. Don\'t forget a smiley :) or :( \'cos that\'s how we talk nowadays ')
new_lang = {':)': b'\xf0\x9f\x98\x83'.decode('utf-8'),
            ':(': b'\xE2\x98\xB9'.decode('utf-8')
            }
phrase = phrase.split()
i=0
for x in new_lang:
    for i in range(len(phrase)):
        if x == phrase[i]:
            phrase[i] = new_lang[x]
phrase = ' '.join(phrase)
print(phrase)












