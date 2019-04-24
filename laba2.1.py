str = input()
lst = str.split()
m=len(lst)
g=[]
for i in range(m):
    t=len(lst[i])
    if t>5 and lst[i][5]!=",":
        g.append(lst[i])
print(g)

