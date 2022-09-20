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

my_list = input("Enter the sequence (separated by commas): \r\n").replace(' ','').split(',')

result_list = []

for i in my_list:
    flag = False
    for j in result_list:
        if j == i:
            flag = True
            break
    if flag:
        continue
    else:
        result_list.append(i)

print(result_list)