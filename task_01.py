# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

import math
d = float(input('задайте точность d = 0.____: '))


def pi(): #1
    p = 3
    for i in range(2, 50, 4):
        p+= 4/(i*(i+1)*(i+2) - 4/((i+2)*(i+3)*(i+4)))
    return p

cnt = pi()//d*d
print(cnt)

def gauss_Pi(d): #2
    accuracy = 1
    pi_Gauss = 48*math.atan(1/18)+32*math.atan(1/57)-20*math.atan(1/239)
    number_of_digit = int(len(str(d).split(".")[1]))
    # print(number_of_digit)
    while number_of_digit > 0:
        accuracy*=10
        number_of_digit-=1
    return int(pi_Gauss*accuracy)/accuracy
print(gauss_Pi(d))
