# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]
a = int(input('введите число: '))


def mnozh(a: int, lst=[], count=2):
    if a == 1:
        return lst
    if a % count == 0:
        lst.append(count)
        while a % count == 0:
            a = a/count
    return mnozh(a, lst, count+1)


print(mnozh(a))
