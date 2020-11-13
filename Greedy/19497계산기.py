n=int(input())
ans=[]
while n:
    if n&1:
        ans.append('[/]')
        n*=2
    elif n&2:
        ans.append('[+]')
        n-=2
    else:
        ans.append('[*]')
        n=n//2
print(len(ans))
print(*ans[::-1])

