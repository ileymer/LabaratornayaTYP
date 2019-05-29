import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
a=""
while(a!="0"):
    print("datatime - Дата и время")
    print("1 - (a^2/b^2 + c^2*a^2)/(a+b+c*(k-a/b^3)) + c + (k/b -k/a)*c")
    print("2 - Вычислить определитель матрицы 3х3")
    print("3 - Вывод Поступившего ранее сообщения")
    print("4 - 2х2 матрица увеличенная в detA")
    print("0 - Выход")

    a=input('Введите номер действия: ')
    sock.send(a.encode())
    if a=="datatime":
        data=sock.recv(1024)
        print(data.decode())
    if a=="1":
        aa=input("Введите число а = ")
        sock.send(aa.encode())
        b=input("Введите число b = ")
        sock.send(b.encode())
        c=input("Введите число с = ")
        sock.send(c.encode())
        k=input("Введите число k = ")
        sock.send(k.encode())
        rs=sock.recv(1024)
        print("Ответ=", rs.decode())
    if a=="2":
        print("Введите матрицу 3х3 через enter:")
        m=[]
        for i in range(9):
            m.append(input())
            sock.send(m[i].encode())
        o=sock.recv(1024)
        print("Определитель матрицы = ",o.decode())
    if a=="3":
        so=input("введите сообщение - ")
        sock.send(so.encode())
        print("Ранее отправленное сообщение:" , sock.recv(1024).decode())
    if a=="4":
        print("Введите матрицу 2х2 через enter:")
        a1=input()
        sock.send(a1.encode())
        a2=input()
        sock.send(a2.encode())
        
        a3=input()
        sock.send(a3.encode())
        a4=input()
        sock.send(a4.encode())
        a1=sock.recv(1024).decode()
        print(a1)
        a2=sock.recv(1024).decode()
        print(a2)
        a3=sock.recv(1024).decode()
        print(a3)
        a4=sock.recv(1024).decode()
        print(a4)
    print("___________________________________________________")
    print(" ")
     
   
    

sock.close()
ddr=input()
