# 2- Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

num =(input('Задайте последовательность чисел: ').split())
def quit(n):
    lst=[]
    for i in n:
        if n.count(i)==1:
            lst.append(i)
    return lst
print(quit(num))