def div(a, b):
    # Because this problem thinks -1//3 is 0, which should be actually -1
    if (a<0) ^ (b<0): return -(-a//b)
    return a//b

def minmax(index, st):
    if index == n-1:
        return st,st
    m = float('inf')
    M = -m
    nxt = num[index+1]
    ns = [st+nxt, st-nxt, st*nxt, div(st,nxt)]
    for i in range(4):
        if op[i] == 0:
            continue
        op[i]-= 1
        mnew, Mnew = minmax(index+1, ns[i])
        m = min(m, mnew)
        M = max(M, Mnew)
        op[i]+= 1
    return m, M

n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))
m, M = minmax(0, num[0])
print(M)
print(m)