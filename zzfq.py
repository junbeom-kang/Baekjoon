a={}
a[1]={}
a[1][1]={}
a[1][1]=3
a[1][2]=4
del a[1][2]
print(a[1])
for i in a[1].values():
    print(i)