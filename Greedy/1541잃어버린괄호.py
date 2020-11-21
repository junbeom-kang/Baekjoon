a=input()
b=a.split('-')
ans=0
for i in range(len(b)):
    sum=0
    x=b[i].split('+')
    for j in x:
        sum+=int(j)
    if i==0:
        ans=sum
    else:
        ans-=sum
print(ans)
