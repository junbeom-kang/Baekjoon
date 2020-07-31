n=int(input())
a=[0for i in range(n+1)] #n+1로 해야하는이유==1일때 하나밖에없는대 참고할수가없잖아
a[0]=1
a[1]=2
for i in range(2,n):
    a[i]=a[i-1]+a[i-2]
    print(a[i], a[i - 1], a[i - 2])
print(a[n-1]%10007)
