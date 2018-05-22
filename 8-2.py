x=-1
a=input("문자열 : ")
for i in range(len(a)):
    x+=1
    print(a[x],end="")
print("")
y=len(a)
for k in range(len(a)):
    y-=1
    print(a[y],end="")
