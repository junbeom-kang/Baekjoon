import sys
from heapq import *
input=sys.stdin.readline
weight=list(map(float,input().split()))
dic={'A':weight[0],'B':weight[1],'C':weight[2],'D':weight[3],'E':weight[4]}
Y=[]
O=[]
n,m=map(int,input().split())
arr=[[] for _ in range(n)]
arr_weight=[[] for _ in range(n)]
for i in range(n):
    arr[i]=list(input().rstrip())
for i in range(n):
    arr_weight[i]=list(input().rstrip())
for i in range(n):
    for j in range(m):
        if arr[i][j]=='W':
            continue
        elif arr[i][j]=='Y':
            heappush(Y,(-dic[arr_weight[i][j]],i,j,arr_weight[i][j]))
        else:
            heappush(O,(-dic[arr_weight[i][j]],i,j,arr_weight[i][j]))
while Y:
    temp=heappop(Y)
    print(temp[3],-temp[0],temp[1],temp[2])
while O:
    temp = heappop(O)
    print(temp[3], -temp[0], temp[1], temp[2])
