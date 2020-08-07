import sys
input=sys.stdin.readline
n=int(input())
first=list(map(int,input().split()))
first.sort()
m=int(input())
second=list(map(int,input().split()))
def checkleft(left,leftR,first,i):
    if first[left]==i and first[leftR]==i:
        return left
    while left<=leftR:
        mid = (left + leftR) // 2
        if first[mid]==i:
            return checkleft(left,mid-1,first,i)
        elif first[mid]>i:
            leftR=mid-1
        else:
            left=mid+1
    return leftR+1

def checkright(right,rightL,first,i):
    if first[right]==i and first[rightL]==i:
        return right
    while rightL<=right:
        mid = (rightL + right) // 2
        if first[mid]==i:
            return checkright(right,mid+1,first,i)
        elif first[mid]>i:
            right=mid-1
        else:
            rightL=mid+1
    return rightL-1


def check(i,first):
    left=0
    right=len(first)-1
    if first[left]==i and first[right]==i:
        return right-left+1
    while left<=right:
        mid=(left+right)//2
        if first[mid]==i:
            if left==right:
                return 1
            else:
                index=checkleft(left,mid-1,first,i)
                index1=checkright(right,mid+1,first,i)
                return index1-index+1
        elif first[mid]>i:
            right=mid-1
        else:
            left=mid+1
for i in second:
    x=check(i,first)
    if x==None:
        print(0,end=' ')
    else:
        print(x,end=' ')
