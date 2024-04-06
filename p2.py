# parsing slovarya
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("values", nargs='*')
parser.add_argument('--sort', dest='sort', action='store_true')
args = parser.parse_args()
sp = {a.split('=')[0]: a.split('=')[1] for a in args.values}
if args.sort:
    sp = dict(sorted(sp.items()))
for a in sp:
    print(f'Key: {a} Value: {sp[a]}')
