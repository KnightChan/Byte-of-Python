__author__ = 'Qingjun'

# Filename : using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = open('data\\poem.txt', 'w')
f.write(poem)
f.close()

f = open('data\\poem.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()