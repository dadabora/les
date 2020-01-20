from itertools import cycle
x = input('Введите символы -  ')
my_list = list(x)
print(my_list)

for el in cycle(my_list):

    
    print(el)
