# calculator 2.0
import sys

if len(sys.argv) > 1:
    a = 1
    c = 0
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isdigit() and float(sys.argv[i]).is_integer():
            c += int(sys.argv[i]) * a
            a *= -1
        elif sys.argv[i].isdigit():
            c = 0
            a = 2
            break
        else:
            a = 3
            print('ValueError')
            break
    if a == 1 or a == -1:
        print(c)
else:
    print("NO PARAMS")
