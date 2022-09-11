# my_list = [1,2,34,'hello','anup']
# sec_list = ['hey','kai','krtos']

# def My_loops(value):
#     for i in value:
#         print('this is ur value :' + str(i))

# My_loops(my_list)
# My_loops(sec_list)
# My_loops(sec_list)
##################################################################

def My_loops(value):
    for i in value:
        print('this is ur value :' + str(i))

def myList(nums):
    my_list = [1,2,34,'hello','anup']
    my_list.append(nums)
    My_loops(my_list)

myList('shedge')
