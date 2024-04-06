# predskasatel pola
import sys
import argparse

parser = argparse.ArgumentParser(
    description="test args")


parser.add_argument('--barbie',
                    type=int,
                    default=50)
parser.add_argument('--cars',
                    type=int,
                    default=50)
parser.add_argument('--movie',
                    default='other',
                    choices=['melodrama', 'football', 'other']                    choices=['melodrama', 'football', 'other'])
)

my_args = parser.parse_args()
if my_args.barbie not in range(101):
    my_args.barbie = 50
if my_args.cars not in range(101):
    my_args.cars = 50
d = {'football': 100, 'melodrama': 0, 'other': 50}
boy = int((100 - my_args.barbie + my_args.cars + d[my_args.movie]) / 3)
girl = 100 - boy
print(f"boy: {boy}")
print(f"girl: {girl}")
