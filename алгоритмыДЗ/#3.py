# задача под номером 3
def numJS(j, s):
    a = 0

    for i in s:
        for j in j:
            if i == j:
                a += 1
    return a

print(numJS("aA", "aAAbbbb"))
#сначала приравниваем счетчик к нулю после смотрим в камни проходим по каждому из них и если есть совпадение
#инкрементируем счетчик и возвращаем его