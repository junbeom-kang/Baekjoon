n=int(input())
ans=[0for i in range(n+1)]
ans[0]=1
ans[1]=3
for i in range(2,n):
    ans[i]=ans[i-2]*2+ans[i-1]
print(ans[n-1]%10007)