# raschot pl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--per-day", dest='per_day', type=int, default=0)
parser.add_argument("--per-week", dest='per_week', type=int, default=0)
parser.add_argument("--per-month", dest='per_month', type=int, default=0)
parser.add_argument("--per-year", dest='per_year', type=int, default=0)
parser.add_argument("--get-by", dest='get', type=str, default='day', choices=['day', 'month', 'year'])
args = parser.parse_args()
if args.get == 'day':
    print(int(args.per_day + (args.per_week / 7) + (args.per_month / 30) + (args.per_year / 360)))
elif args.get == 'month':
    print(int(args.per_day * 30 + (args.per_week * 30 / 7) + args.per_month + args.per_year / 12))
else:
    print(int(args.per_day * 360 + (args.per_week * 360 / 7) + args.per_month * 12 + args.per_year))
