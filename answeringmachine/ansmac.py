def main(a):
    b = ['Расп', 'расп', 'Стои', 'стои', 'Тел', 'тел', 'Адр', 'адр']
    if b[0] in a or b[1] in a:
        timetable()
    if b[2] in a or b[3] in a:
        price()
    if b[4] in a or b[5] in a:
        info()
    if b[6] in a or b[7] in a:
        adress()

def timetable():
    print('Распсиание работы зала\nВт - 18:00\nСр - 17:00\nПт - 19:00')
    print('Вы хотите записаться на тренировку? Введите - ДА/НЕТ')
    t1 = input()
    s1 = {}
    if t1 == 'Да' or t1 == 'да' or t1 == 'ДА':
        print('Введите день недели на который вы хотите записаться')
        t2 = input()
        print('Введите удобное для вас время с 8 до 22')
        t3 = int(input())
        if 8 < t3 < 22:
            s1[t2] = t3
            print('Вы записанны на', s1)
def price():
    print('Оплата в месяц будет составлять - 3333')
def info():
    print('Номер телефона вашего тренера - 89666777888')
def adress():
    print('г.Сочи ул.Воскресенская д.12')