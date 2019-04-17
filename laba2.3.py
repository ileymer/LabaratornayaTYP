my_string =input()
a=my_string.split(";")
k=len(a)
for i in range(k-2):
    if a[i][1]=="П" and a[i][2]=="е" and a[i][3]=="т" and a[i][4]=="р" and a[i][5]=="о" and a[i][6]=="в" and a[i][7]==" ":
        t=a[i].split()


        print("Петров",t[1],t[2],a[i+1],a[i+2])




