#задача под номером 1

def num(numbers):
    a = 0

    while numbers:
        if numbers % 2 == 0:
            numbers /= 2
            a += 1
        else:
            numbers -= 1
            a += 1
    return a

print(num(14))
print(num(8))
print(num(123))
  # счетчик равен 0 - a = 0
  #вводим цикл while пока число не равно 0 если четное то делим на 2 если нечетеное то вычитаем единичку после чего a +=1
  # затем возвращаем кол-во итераций - return a

