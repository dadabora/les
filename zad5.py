from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)
pro_all = reduce(lambda x,y: x * y, my_list)
print(pro_all)