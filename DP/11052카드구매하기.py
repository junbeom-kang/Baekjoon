import sys
def input():
    return sys.stdin.readline()
n=int(input())
arr=[0]+list(map(int,input().split()))
ans=[0]*(n+1)
ans[1]=arr[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        ans[i]=max(ans[i],ans[i-j]+arr[j])
print(ans[n])