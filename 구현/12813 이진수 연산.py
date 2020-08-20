def aa(x):
    for i in x:
        if i=='0':
            print(1,end='')
        else:
            print(0,end='')
a=int(input(),2)
b=int(input(),2)
print(bin(a&b)[2:].zfill(100000))
print(bin(a|b)[2:].zfill(100000))
print(bin(a^b)[2:].zfill(100000))
aa(bin(a)[2:].zfill(100000))
print()
aa(bin(b)[2:].zfill(100000))
