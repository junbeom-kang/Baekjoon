import sys
input=sys.stdin.readline
n=int(input())
up = [2 * n]
down = [2 * n - 2]
if n!=1:
    ans=0
    sum=0
    temp=(2*n-4)//2
    t=1
    for i in range(1,2*n+1):
        sum+=i
    sum-=2*n-3
    ans+=sum*t
    t+=1
    for i in range(2*n-4,2*n-4-temp,-1):
        sum-=i
        ans+=sum*t
        t+=1
    sum-=2*n-2
    ans+=sum*t
    t+=1
    sum -= (2 * n - 1)
    ans += sum * t
    t+=1
    for i in range(n-2,n-2-temp,-1):
        sum-=i
        ans+=sum*t
        t+=1

    for i in range(1,n-1):
        up.append(i)
    up.append(2*n-1)
    for i in range(n-1,(2*n)-3):
        down.append(i)
    down.append(2*n-3)
    print(ans)
    print(*up)
    print(*down)

else:
    print(2)
    print("2 1")
