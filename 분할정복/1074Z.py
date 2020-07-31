import sys
sys.setrecursionlimit(10**6)
N,r,c=list(map(int,sys.stdin.readline().split()))
ans=0


def count(a,b,n):
    global ans
    for i in range(2):
        for j in range(2):
            na=a+i
            nb=b+j
            #print(na,nb,ans)
            if na==r and nb==c:
                print(ans)
                sys.exit()
            ans = ans + 1


def divide(a,b,n):
    if n==1:
        count(a,b,n)
    else:
        m=n//2
        divide(a,b,m)
        divide(a,b+n,m)
        divide(a+n,b,m)
        divide(a+n,b+n,m)

divide(0,0,2**N)