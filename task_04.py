# Задана натуральная степень n.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
# *Пример: n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from hashlib import new
from operator import truediv
import random
number_N = int(input('Input number: '))
test_bool = True
while test_bool:
    list_1 = [random.randint(0, 100) for i in range(number_N+1)]
    if list_1[0] != 0:
        test_bool = False

list_2 = ['x' for i in range(number_N+1)]

result = ''

for i in range(0, len(list_1)):
    if list_1[i] == 1 and number_N>1:
        result += f"{list_2[i]}^" + f"{number_N}"
    elif list_1[i] != 0 and number_N>1:
        result += f"{list_1[i]}*" + f"{list_2[i]}^" + f"{number_N}"
    elif list_1[i] == 1 and number_N==1:
        result += f"{list_2[i]}"
    elif list_1[i] == 1 and number_N==0:
        result += f"{list_1[i]}"
    elif list_1[i] != 0 and number_N==1:
        result += f"{list_1[i]}*" + f"{list_2[i]}"
    elif list_1[i] != 0 and number_N==0:
        result += f"{list_1[i]}"
    if i < len(list_1)-1:
        if result[-3:len(result)] != " + ":
            result += " + "
    number_N -= 1
result += " = 0"
print(result)

# с использованием zip

number_N = int(input('Input number: '))
test_bool = True
while test_bool:
    coef_1 = list(map(str,[random.randint(0,100) for i in range(0,number_N+1)]))
    if coef_1[0] !='0':
        test_bool=False

coef_2 = list(map(str,['x' if i < number_N else '' for i in range(0,number_N+1)]))
coef_3 = list(map(str,[i if i>1 else '' for i in range(number_N,-1,-1)]))

new_list=list(zip(coef_1, coef_2, coef_3))

for i,item in enumerate(new_list): # i - index, item - element value
    new_list[i] = list(filter(lambda a: a!="", new_list[i]))
    print(new_list[i])
    new_list[i] = "*".join(list(map(str, item)))
list_final=" + ".join(new_list)
print(list_final)
