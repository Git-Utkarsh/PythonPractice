import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")
args = parser.parse_args()
print(args.arg1 + " is first argument and " + args.arg2 + " is second argument")


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()
print(args.optional)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("positional", help="description of positional argument")
args = parser.parse_args()
print(args.positional)
