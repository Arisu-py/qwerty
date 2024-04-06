# sosdanie i ispolzovanie modulei
import argparse
import os


def count_lines(p):
    if os.access(p, os.F_OK):
        with open(p) as in_file:
            lines = [line.rstrip('\n') for line in in_file.readlines()]
        return len(lines)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='file')
    my_args = parser.parse_args()
    print(count_lines(my_args.file))
