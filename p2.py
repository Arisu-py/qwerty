# kopirovanie filov
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source_file")
parser.add_argument("source_receiver")
parser.add_argument('--upper', dest='up', action='store_true')
parser.add_argument('--lines', dest='line')
args = parser.parse_args()
with open(args.source_file) as in_file:
    lines = [line for line in in_file.readlines()]
if args.line:
    if int(args.line) > len(lines):
        args.line = len(lines)
    lines = lines[:int(args.line)]
if args.up:
    lines = [a.upper() for a in lines]
with open(args.source_receiver, 'w') as out_file:
    print(*lines, sep='', end='', file=out_file)
