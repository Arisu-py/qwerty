# super parser
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
my_args = parser.parse_args()
if my_args.arg:
    print(*my_args.arg, sep='\n')
else:
    print('no args')
