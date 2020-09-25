import sys
def bisect(v):
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if data1[mid]==v:
            return True
        elif data1[mid]<v:
            left=mid+1
        else:
            right=mid-1
    return False


input=sys.stdin.readline
n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))
data1.sort()
for i in data2:
    if bisect(i):
        print('1',end=' ')
    else:
        print('0',end=' ')