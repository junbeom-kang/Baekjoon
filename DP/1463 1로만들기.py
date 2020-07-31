n=int(input())
a=[0for i in range(n+1)]
a[1]=0
for i in range(2,n+1):
    a[i]=a[i-1]+1
    if i%2==0 and a[i]>a[i//2]+1:
        a[i]=a[i//2]+1
    if i%3==0 and a[i]>a[i//3]+1:
        a[i]=a[i//3]+1
print(a[n])
print(a)