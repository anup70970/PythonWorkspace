from msilib.schema import Binary


currentyr = input('type the current year\n')

bornyr = input('type the year you born\n')

try:
    print('You are',int(currentyr) - int(bornyr),'years old')
except(ValueError):
    print('please enter valid number')