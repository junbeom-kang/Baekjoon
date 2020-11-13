import sys
input=sys.stdin.readline
n, m = map(int, input().split())
def divide(what,n):
    ans=0
    while what>=n:
        what//=n
        ans+=what
    return ans
print(min(divide(n,5)-divide(n-m,5)-divide(m,5),divide(n,2)-divide(n-m,2)-divide(m,2)))