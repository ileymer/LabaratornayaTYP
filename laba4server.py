import datetime
import socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
so="Поступившего ранее сообщения не было"
print('connected:', addr)
a=""
while(a!="0"):
    a = conn.recv(1024)
    a=a.decode()

    if a=="datatime":
        today = datetime.datetime.today()
        data=today.strftime("%Y-%m-%d-%H.%M.%S")
        conn.send(data.encode())
    if a=="1":
        aa= conn.recv(1024)
        b = conn.recv(1024)
        c = conn.recv(1024)
        k = conn.recv(1024)
        aa=int(aa.decode())
        b=int(b.decode())
        c=int(c.decode())
        k=int(k.decode())
        if ((aa!=0 and b!=0)) and (aa+b+c*(k-aa/b**3)!=0):
            rs=1-(aa**2/b**2 + c**2*aa**2)/(aa+b+c*(k-aa/b**3)) + c + (k/b -k/aa)*c
            conn.send(str(rs).encode())
        else:
            rq="Ошибка: деление на 0"
            conn.send(rq.encode())
    if a=="2":
        m=[]
        for i in range(9):
            m.append(conn.recv(1024))
            m[i]=int(m[i].decode())
            print(m[i])
        o=m[0]*m[4]*m[8]+m[1]*m[5]*m[6]+m[2]*m[3]*m[7]-m[2]*m[4]*m[6]-m[1]*m[3]*m[8]-m[0]*m[5]*m[7]
        conn.send(str(o).encode())
    if a=="3":
      
        conn.send(so.encode())
        so=conn.recv(1024)
        so=so.decode()
      
    if a=="4":
        a1= int(conn.recv(1024))
        a2 = int(conn.recv(1024))
        a3 = int(conn.recv(1024))
        a4 = int(conn.recv(1024))
        op=(a1*a4)-(a2*a3)
        a1=a1*op
        conn.send(str(a1).encode())
        print("")
        a2=a2*op
        conn.send(str(a2).encode())
        print("")
        a3=a3*op
        conn.send(str(a3).encode())
        print("")
        a4=a4*op
        conn.send(str(a4).encode())
    
    
        
d=input()
conn.close()

