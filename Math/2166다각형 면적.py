import sys
input=sys.stdin.readline
def sinbal(a,b,c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])


n=int(input())
adj=[]
temp=0
for _ in range(n):
    a,b=map(int,input().split())
    adj.append((a,b))
for i in range(n-2):
    temp+=sinbal(adj[0],adj[i+1],adj[i+2])

print(round(abs(temp/2),1))