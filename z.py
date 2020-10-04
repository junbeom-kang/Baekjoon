import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    ans=0
    n=int(input())
    visited=[-1]*n
    stud=list(map(int,input().split()))
    for i in range(n):
        if stud[i]==i+1:
            visited[i]=2
        elif visited[i]==-1:
            temp=i
            while 1:
                if stud[temp]==temp+1:
                    print('sex',i)
                    break
                elif visited[temp]==1:
                    visited[temp]=2
                    temp=stud[temp]-1
                elif visited[temp]==-1:
                    visited[temp]=1
                    temp=stud[temp]-1
                else:
                    break
        print(i,visited)
    print(visited,'!')
    for i in visited:
        if i==2:
            ans+=1
    print(n-ans)






