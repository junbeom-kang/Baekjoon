import sys
input=sys.stdin.readline
n=int(input())
first=list(map(int,input().split()))
first.sort()
m=int(input())
second=list(map(int,input().split()))
def check(i,first):
    cnt=0
    left=0
    L=True
    R=True
    right=len(first)-1
    while left<=right:
        mid=(left+right)//2
        if first[mid]==i:
            temp=mid-1
            while first[mid]==i and L:
                mid+=1
                cnt+=1
                if mid==len(first):
                    break
            while first[temp]==i and R:
                temp-=1
                cnt+=1
                if mid==-1:
                    R=False
            break
        elif first[mid]>i:
            right=mid-1
        else:
            left=mid+1
    return cnt
for i in second:
    print(check(i,first),end=' ')
