# Filename : break.py

while True:
    s = input('Enter something : ')
    if (s == 'quit'):
        break
    print('Length of the string is', len(s))
else:
    print('the while loop is over.')
print('Done!')
