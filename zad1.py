
from sys import argv

script_name, first_param, second_param, third_param = argv


print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)

print('Итого= ', (int(first_param)*int(second_param))+int(third_param))
