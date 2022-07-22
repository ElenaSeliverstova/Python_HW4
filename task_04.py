# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.


file = open('Text.txt', "w", encoding='utf-8')
file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
file.close()

path = 'Text.txt'

def delete_nums(path: str) -> str:

    file = open('Text.txt' , "r",encoding='utf-8')
    data = file.read()
    list_of_words = data.split()
    file.close()

    new_list = []
    for i in list_of_words:
        delete_bool = False
        for n in i:
            if n.isdigit():
                delete_bool = True
                break
        if delete_bool == False:
            new_list.append(i)

    return  f"{list_of_words} -> " + " ".join(new_list) 
    
print(delete_nums(path))
