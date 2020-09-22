import sys
import heapq
input=sys.stdin.readline
n=int(input())
parent=[i for i in range(n+1)]
adj=[[]for _ in range(n+1)]
level=[[]for _ in range(n+1)]
x=1
print(parent)
for _ in range(n):
    a,b,c=map(int,input().split())
    adj[a].extend([b,c])
    if b!=-1:
        parent[b]=a
    if c!=-1:
        parent[c]=a
def findroot(v):
    if parent[v]==v:
        return v
    else:
        findroot(parent[v])

def preorder(v,cnt):
    global x
    if adj[v][0]==-1 and adj[v][1]==-1:
        level[cnt].append(x)
        x+=1
    else:
        if adj[v][0]!=-1:
            preorder(adj[v][0],cnt+1)
        level[cnt].append(x)
        x+=1
        if adj[v][1]!=-1:
            preorder(adj[v][1],cnt+1)
print(findroot(1))
preorder(findroot(1),1)
ans=[]
for i in range(len(level)):
    if level[i]:
        if len(level[i])==1:
            heapq.heappush(ans,(-1,i))
        else:
            heapq.heappush(ans,(-(level[i][-1]-level[i][0]+1),i))
temp=heapq.heappop(ans)
print(temp[1],-temp[0])