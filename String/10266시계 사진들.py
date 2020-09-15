import sys
input=sys.stdin.readline
def makeTable(pattern):
    LP=len(pattern)
    table=[0]*LP
    j=0
    for i in range(1,LP):
        while j>0 and pattern[j]!=pattern[i]:
            j=table[j-1]
        if pattern[j]==pattern[i]:
            j+=1
            table[i]=j
    return table


def makegap(L):
    L.sort()
    make=[]
    for i in range(len(L)-1):
        make.append(L[i+1]-L[i])
    make.append(L[0]+360000-L[-1])
    return make


def solution(n,first,second):
    first=makegap(first)
    second=makegap(second)
    table=makeTable(second)
    j=0
    for i in range(2*n-1):
        if i>=n:
            i-=n
        while j>0 and first[i]!=second[j]:
            j=table[j-1]
        if first[i]==second[j]:
            if j==n-1:
                return True
            else:
                j+=1
    return False


n=int(input())
first=list(map(int,input().split()))
second=list(map(int,input().split()))
ans=solution(n,first,second)
if ans:
    print('possible')
else:
    print('impossible')
