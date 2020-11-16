import sys
def fenwic_find(tree, idx):
    res = 0
    while idx < n + 1:
        res += tree[idx]
        idx += (idx & -idx)
        print('res',res)
        print('fenwic',idx)
    return res

def fenwic_update(tree, idx, d):
    print('upindex',idx)
    while idx > 0:
        tree[idx] += d
        idx -= (idx & -idx)
        print(idx)
    print

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
tr = [0] * (max(arr) + 1)
ans = 0
for i in range(n):
    print(tr,arr[i])
    ans += fenwic_find(tr, arr[i])
    fenwic_update(tr, arr[i], 1)
    print(tr)
    print()
print(tr)
print(ans)