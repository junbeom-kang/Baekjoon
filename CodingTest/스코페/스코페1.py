#01~신경써야함
import sys
def make(a,b):
    left=[a[0],b[0]]
    left.sort()
    right=[a[1],b[1]]
    right.sort()
    if right[0][0]<left[1][0]:
        return -1
    elif right[0][0]==left[1][0] and left[1][1]>right[0][1]:
        return -1
    else:
        return left[1],right[0]

n=int(input())
if n==1:
    ans=input()
    print(ans)
else:
    temp=[0]*n
    for i in range(n):
        a,_,b=(input().split())
        temp[i]=((int(a.split(":")[0]),int(a.split(":")[1])),((int(b.split(":")[0]),int(b.split(":")[1]))))
    t=make(temp[0],temp[1])
    if t==-1:
        print(-1)
        sys.exit()
    for i in range(1,n-1):
        t=make(temp[i+1],t)
        if t==-1:
            print(-1)
            sys.exit()

    print("%02d:%02d ~ %02d:%02d"%(t[0][0],t[0][1],t[1][0],t[1][1]))



