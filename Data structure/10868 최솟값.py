import sys
import math
#find
def find(left,right,start,end,v):
    if start<=left and right<=end:
        return tree[v]
    elif start>right or left>end:
        return INF
    else:
        mid=(left+right)//2
        return min(find(left,mid,start,end,2*v),find(mid+1,right,start,end,2*v+1))

INF=sys.maxsize
input=sys.stdin.readline
n,m=map(int,input().split())
size=2**math.ceil(math.log2(n))
tree=[INF]*(size*2)
for i in range(size,size+n):
    tree[i]=int(input())
for i in range(size-1,0,-1):
    tree[i]=min(tree[2*i],tree[2*i+1])

for i in range(m):
    a,b=map(int,input().split())
    print(find(1,size,a,b,1))
"""
최솟값 한정 좋은풀이
import sys
input = sys.stdin.readline
print = sys.stdout.write


def find_min(start, end):
    ret = max_val

    while start <= end:
        if start%2 == 1: ret = min(ret, tree[start])
        if end%2 == 0: ret = min(ret, tree[end])

        start = (start + 1) // 2
        end = (end - 1) // 2

    return ret


max_val = 2148473647
n, m = map(int, input().split())
tree = [max_val] * (4*n)

# 1. idx
idx = 1
while idx < n:
    idx *= 2
idx -= 1

# 2. 리프노드에 수 입력받기
for i in range(1, n+1):
    tree[i+idx] = int(input())

# 3. min index tree 구성하기
for i in range(idx, 0, -1):
    tree[i] = min(tree[i*2], tree[i*2+1])

for _ in range(m):
    a, b = map(int, input().split())
    print("%d\n" % find_min(a+idx, b+idx))

"""
