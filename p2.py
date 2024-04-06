# kalculyator 30
import argparse

parser = argparse.ArgumentParser(
    description="test args")

parser.add_argument('ar', nargs='*')
args = parser.parse_args()

if not args.ar:
    print("NO PARAMS")
elif len(args.ar) == 1:
    print("TOO FEW PARAMS")
elif len(args.ar) > 2:
    print("TOO MANY PARAMS")
else:
    if args.ar[0].isdigit() and args.ar[1].isdigit():
        print(int(args.ar[0]) + int(args.ar[1]))
    else:
        print('ValueError')
