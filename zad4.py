# путь как я думал
def func(z):
    x = 0
    super_new_list = []
    while x != len(z):

        a = z[x]
        x += 1
        i = z.count(a)
        if i > 1:
            continue
        super_new_list.append(a)

    return super_new_list


my_list = [2, 5, 4, 43, 43, 3, 2, 5, 34, 5, 34, 23]
# генератор который собрал после
data = [i for i in my_list if my_list.count(i) == 1]

print(my_list)
print(func(my_list))
print(data)