# super cat
import sys
import os

test = sys.argv[1:]
name = ''
for el in test:
    if '.txt' in el:
        name = el
if os.access(name, os.F_OK):
    with open(name) as in_file:
        lines = [line.rstrip('\n') for line in in_file.readlines()]
    if '--sort' in test:
        lines.sort()
        test.pop(test.index('--sort'))
    if len(test) > 1:
        f = True
        if '--num' in test:
            for i in range(len(lines)):
                print(i, lines[i])
            f = False
        if '--count' in test:
            if f:
                print(*lines, sep='\n')
            print(f'rows count: {len(lines)}')
    else:
        print(*lines, sep='\n')
else:
    print('ERROR')

