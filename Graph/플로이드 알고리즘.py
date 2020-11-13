import sys

def input():
    return sys.stdin.readline()

max_value=float('inf')
n=int(input())
m=int(input())
price=[[max_value for _ in range(n)]for _ in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    price[a-1][b-1]=min(price[a-1][b-1],c)
for i in range(n):
    price[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            price[i][j]=min(price[i][j],price[i][k]+price[k][j])
for i in price:
    for j in i:
        if j==max_value:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()