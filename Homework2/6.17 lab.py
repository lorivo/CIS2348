# Lori Vo 1852113

givenpass_og = input('')
givenpass_new = ''

for n in range(len(givenpass_og)):
    if givenpass_og[n] == 'i':
        givenpass_new += '!'
        continue
    elif givenpass_og[n] == 'a':
        givenpass_new += '@'
        continue
    elif givenpass_og[n] == 'm':
        givenpass_new += 'M'
        continue
    elif givenpass_og[n] == 'B':
        givenpass_new += '8'
        continue
    elif givenpass_og[n] == 'o':
        givenpass_new += '.'
        continue
    else:
        givenpass_new += givenpass_og[n]

givenpass_new += 'q*s'

print(givenpass_new)
