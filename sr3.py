import os.path
import sys
import os


def exit():
    m = input('Вы хотите продолжить? (yes/no)')
    if m == 'yes':
        menu()
    else:
        sys.exit()

def menu():
    print('0 - Выход\n1 - Посчитать файлы в директории\n2 - Вывод информации по названию'
           '\n3 - Изменение количества товаров указанных номеров')
    gg = input('>>')
    if gg == '0':
        sys.exit()
    if gg == '1':
        files()
    if gg == '2':
        vivodn()
    if gg == '3':
            izmena()


def files():
    di = input('Введите адрес директории: ')
    print('Файлов в директории:', len([name for name in os.listdir(di) if os.path.isfile(os.path.join(di, name))]))
    exit()

def vivodn():
    f = open('products.txt', 'r')
    a = []
    n = 0
    for i in f:
        a.append(i)
        n = n + 1
    rt=[]
    d = []
    q = []
    g = []
    for i in range(n):
        d.append(a[i].split(";"))
        g.append(str(d[i][1]))

    g = sorted(g)
    for i in range(n):
        for j in range(n):
            if g[i] == d[j][1]:
                q.append(j)
        print(d[q[i]][0] + ";" + d[q[i]][1] + ";" + d[q[i]][2] + ";" + str(int(d[q[i]][3])))
        rt.append(d[q[i]][0] + ";" + d[q[i]][1] + ";" + d[q[i]][2] + ";" + str(int(d[q[i]][3])))
    print("Сохранить файл в отсортированном виде? yes/no")
    ws = input()
    if ws=="yes":
        print('укажите путь - ')
        qw=str(input())
        f=open(qw, 'w')
        for i in range(n):
            f.write(rt[i] + '\n')
        f.close()


    exit()


def izmena():
    n = 0
    w = "yes"
    while w == "yes":
        d = []
        g = []
        a = []
        n = 0
        f = open('products.txt', 'r')
        for i in f:
            a.append(i)
            n = n + 1
        for i in range(n):
            d.append(a[i].split(";"))
            g.append('')

        for i in range(n):
            print((d[i][0] + ";" + d[i][1] + ";" + d[i][2] + ";" + str(int(d[i][3]))))
        print(' Введите номер товара, количсетво которого Вы хотите изменить: ')
        p = int(input())
        print(' Введите изменение количества товара: ')
        m = int(input())
        d[p - 1][3] = m
        print("Измененный список:")
        for i in range(n):
            g[i] = d[i][0] + ";" + d[i][1] + ";" + d[i][2] + ";" + str(int(d[i][3]))
            print(g[i])
        f = open('products.txt', 'w')

        for i in range(n):
            if i != (n - 1):
                f.write(g[i] + '\n')
            else:
                f.write(g[i])
        f.close()
        print('  Продолжить изменение количества - yes')
        print('  Выйти в главное меню - back (изменения будут сохранены в любом случае)')
        w = input()
        del a[0]
        del d[0]
        del g[0]

    menu()

menu()






