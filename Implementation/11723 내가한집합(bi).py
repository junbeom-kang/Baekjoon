import sys
input=sys.stdin.readline

def choose(a,b):
    global bi
    n=int(b)
    if a=='add':
        bi=(bi | (1<<(n-1)))
    elif a=='remove':
        bi=(bi&~(1<<(n-1)))
    elif a=='check':
        if (bi&(1<<(n-1))):
            print(1)
        else:
            print(0)
    elif a=='toggle':
        bi=(bi^(1<<(n-1)))
    elif a=='all':
        bi=0b11111111111111111111
    else:
        bi=0b00000000000000000000
n=int(input())
bi = 0b00000000000000000000
for _ in range(n):
    a=input().split()
    if a[0]=='all' or a[0]=='empty':
        choose(a[0],0)
    else:
        choose(a[0],a[1])
