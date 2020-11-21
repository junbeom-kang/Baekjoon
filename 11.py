n=int(input())
if n==64:
    print(1)
else:
    ans=0
    cnt=0
    temp=64
    while ans!=n:
        if ans+(temp>>1)<=n:
            temp=temp>>1
            ans+=temp
            cnt+=1
        else:
            temp=temp>>1
    print(cnt)