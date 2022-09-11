import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--values',type=int,nargs='+',help='please input n number to get sum of n numbers')
args = parser.parse_args()

sum = sum(args.values)
print('sum of numbers are :',sum)