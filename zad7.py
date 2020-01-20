from functools import reduce


def fibo_gen(x):
    my_list = [el for el in range(1, x + 1)]
    print(my_list)
    pro_all = reduce(lambda x, y: x * y, my_list)

    yield pro_all


x = [el for el in fibo_gen(15)]

print(x)


