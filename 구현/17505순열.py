import sys
input=sys.stdin.readline
n,k=map(int,input().split())
yes=[]
no=[]
can=False
for i in range(n-1,-1,-1):
    k=k-i
    if k>0:
        yes.append(i+1)
    elif k<0:
        no.append(i+1)
        k+=i
    elif k==0:
        yes.append(i+1)
        for j in range(i-1,-1,-1):
            no.append(j+1)
        can=True
        break
no=no[::-1]
if can:
    print(*yes+no)
else:
    print(-1)