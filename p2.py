# mega cat
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument('--sort', dest='sort', action='store_true')
parser.add_argument('--num', dest='num', action='store_true')
parser.add_argument('--count', dest='count', action='store_true')
args = parser.parse_args()
if os.access(args.name, os.F_OK):
    with open(args.name) as in_file:
        lines = [line.rstrip('\n') for line in in_file.readlines()]
    if args.sort:
        lines.sort()
    f = True
    if args.num:
        for i in range(len(lines)):
            print(i, lines[i])
        f = False
    if args.count:
        if f:
            print(*lines, sep='\n')
        print(f'rows count: {len(lines)}')
    if not (args.num or args.count):
        print(*lines, sep='\n')
else:
    print('ERROR')
