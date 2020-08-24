import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
g=int(input())
p=int(input())
parent=[]
for i in range(g+1):
    parent.append(i)

def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]
plane=[]
for _ in range(p):
    plane.append(int(input()))
cnt=0
for i in plane:
    k=find(i)
    if k==0:
        break
    parent[k]=k-1
    cnt+=1
print(cnt)