import sys
input=sys.stdin.readline
def check(i,stack):
    left=0
    right=len(stack)-1
    while left<=right:
        mid=(left+right)//2
        if stack[mid]==i:
            return True
        elif stack[mid]>i:
            right=mid-1
        else:
            left=mid+1
    return False

n=int(input())
first=list(map(int,input().split()))
first.sort()
m=int(input())
second=list(map(int,input().split()))
for i in second:
    if check(i,first):
        print(1)
    else:
        print(0)
