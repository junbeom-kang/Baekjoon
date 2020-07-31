import sys
def input():
    return sys.stdin.readline()

n=int(input())
arr=[]
check=[True]*(10001)
for i in range(n):
    p,q=(map(int,input().split()))
    arr.append((p,q))
arr.sort(reverse=True)
print(arr)
sum=0
for i in range(n):
    for j in range(arr[i][1],0,-1):
        if check[j]:
            sum+=arr[i][0]
            check[j]=False
            break
print(sum)