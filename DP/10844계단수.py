n=int(input())
ans=[[0]*10 for i in range(n)]
count=0
for i in range(1,10):
    ans[0][i]=1
for i in range(1,n):
    for j in range(10):
        if j==0:
            ans[i][j]+=ans[i-1][j+1]
            continue
        if j==9:
            ans[i][j]+=ans[i-1][j-1]
            continue
        ans[i][j]+=ans[i-1][j-1]+ans[i-1][j+1]
for i in range(10):
    count=count+ans[n-1][i]
print(count%1000000000)