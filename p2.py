# calculator 1.0
import sys

test = sys.argv[1:]
if len(test) != 2 or not (test[0].isdigit() and test[0].isdigit()):
    print(0)
else:
    print(int(test[0]) + int(test[1]))
