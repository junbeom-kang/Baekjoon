import sys
input=sys.stdin.readline
n=int(input())
ans=set()
for _ in range(n):
    a,b=input().split()
    if b=='enter':
        ans.add(a)
    else:
        ans.remove(a)

for i in sorted(list(ans))[::-1]:
    print(i)