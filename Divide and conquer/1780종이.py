import sys
def input():
    return sys.stdin.readline()
stack=[0,0,0]
n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
count=0
def check(a,b,n):
    temp = arr[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if arr[i][j]!=temp:
                return False
    stack[temp+1]+=1
    return True

def divide(a,b,n):
    if not check(a,b,n):
        m=n/3
        for i in range(3):
            for j in range(3):
                divide(a+i*m,b+j*m,m)
divide(0,0,n)
for i in stack:
    print(i)

