import sys

def input():
    return sys.stdin.readline()

n=int(input())
arr=[]
for i in range(n):
    p,q=map(int,input().split())
    arr.append((p,q))
arr=sorted(arr,key=lambda x:(x[1],x[0]))
count=0
temp=0
for i in range(n):
    if temp<=arr[i][0]:
        count+=1
        temp=arr[i][1]
print(count)