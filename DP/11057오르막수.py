n=int(input())
ans=[[0]*10for i in range(n)]
count=0
for i in range(10):
    ans[0][i]=1
for i in range(1,n):
    for j in range(10):
        if j==0:
            ans[i][j]=ans[i-1][j]
            continue
        for m in range(0,j+1):
            ans[i][j]+=ans[i-1][m]
for i in range(10):
    count=count+ans[n-1][i]
print(count%10007)