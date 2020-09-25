import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=set()
ans=[]
for _ in range(n):
    a.add(input().rstrip())
for _ in range(m):
    temp=input().rstrip()
    if temp in a:
        ans.append(temp)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])