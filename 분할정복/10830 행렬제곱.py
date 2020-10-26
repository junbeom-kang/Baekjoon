import sys
input=sys.stdin.readline
n,m=map(int,input().split())
p=1000
id_matrix=[[0]*n for _ in range(n)]
for i in range(n):
    id_matrix[i][i]=1
def multi(a,b):
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(n):
                sum+=(a[i][k]%p)*(b[k][j]%p)
            temp[i][j]=sum%p
    return temp

def power(adj,k):
    if k==1:
        return multi(adj,id_matrix)
    elif k%2:
        return multi(power(adj,k-1),adj)
    else:
        return power(multi(adj,adj),k//2)


adj=[[]for _ in range(n)]
for i in range(n):
    adj[i]=list(map(int,input().split()))

for i in power(adj,m):
    print(*i)
