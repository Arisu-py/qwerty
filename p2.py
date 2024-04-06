# slovar is parametrov
import sys

test = sys.argv[1:]
sp = {a.split('=')[0]: a.split('=')[1] for a in test if a != '--sort'}
if '--sort' in test:
    sp = dict(sorted(sp.items()))
for a in sp:
    print(f'Key: {a} Value: {sp[a]}')
