import sys
input=sys.stdin.readline
check=[]
n=int(input())
def checkVPS():
    for i in stack:
        if i=='(':
            check.append(i)
        elif i==')':
            if bool(check)==False:
                print('NO')
                return 0
            check.pop()
    if bool(check)==False:
        print('YES')
    elif bool(check)==True:
        print('NO')
for i in range(n):
    stack=input().strip()
    checkVPS()
    check=[]