import sys
import heapq
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
def preorder(v,cnt):
    global x
    if cnt>n+1:
        return
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

n=int(input())
parent = [0]*10001
root = 0
adj=[[]for _ in range(n+1)]
level=[[]for _ in range(n+10)]
x=1
for _ in range(n):
    a,b,c=map(int,input().split())
    adj[a].extend([b,c])
    if b != -1:
        parent[b] += 1
    if c != -1:
        parent[c] += 1
for i in range(1, n+1):
    if parent[i] == 0:
        root = i
preorder(root,1)
ans=[]
for i in range(len(level)):
    if level[i]:
        if len(level[i])==1:
            heapq.heappush(ans,(-1,i))
        else:
            heapq.heappush(ans,(-(level[i][-1]-level[i][0]+1),i))
temp=heapq.heappop(ans)
print(temp[1],-temp[0])