a = input()
a = a.split(";")
q=[]
for i in range(75):
    q.append(" ")



print("  "*2,a[0],end="")
print(a[1],end="")
print(a[2],end="")
print("   "*8,a[4],end="")
print("   "*8,a[3])
t=(len(a)-5)/5
m=5
for j in range(int(t)):
    w=0

    i=1
    r=len(a[m])
    for i in range(r-1):
        q[w]=a[m][i+1]
        w=w+1
    w=w+1
    r=len(a[m+1])
    for i in range(r):
        q[w]=a[m+1][i]
        w=w+1
    w = w + 1
    r = len(a[m + 2])
    for i in range(r):
        q[w] = a[m + 2][i]
        w = w + 1
    w=30
    r = len(a[m + 4])
    for i in range(r):
        q[w] = a[m + 4][i]
        w = w + 1
    w=67
    r = len(a[m + 3])
    for i in range(r):
        q[w] = a[m + 3][i]
        w = w + 1

    m=m+5
    for i in range(74):
        print(q[i], end="")
        q[i]=" "
    print("")








