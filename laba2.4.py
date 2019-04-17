n=int(input("Введите N="))
a=[]
r=1
for i in range(n+2):
    r=i
    a.append(int(0))

for i in range(n):
    print("Введите", i+1 , "элемент: ", end="")
    a[i]=input()

a[-2]=input("Ввеедите новый эелемент: ")
a[-1]=input("Ввеедите новый эелемент: ")

for i in range(n):
    a[i]=a[i+2]


del(a[n+1])
del a[n]
print("Количество эелементов -" ,n)
print("Список",a)

