import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=[]
dp=[0 for _ in range(k+1)]
for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i,k+1):
        if j==i:
            dp[j]+=1
        else:
            dp[j]+=dp[j-i]
print(dp[-1])