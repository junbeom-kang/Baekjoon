import sys
N, K = map(int, sys.stdin.readline().split())
mod = 1000000007
def find(kResult):
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    r1, r2 = kResult, mod
    q = r1//r2
    while r1%r2 != 0:
        r = r1%r2
        r1, r2 = r2, r
        s1, s2 = s2, s1 - s2*q
        t1, t2 = t2, t1 - t2*q
        q = r1//r2

    return (lambda x: x if x > 0 else x + mod)(s2)
def getResult(n, k):
    nResult = 1
    kResult = 1
    for i in range(k):
        nResult *= ((n-i) % mod)
        nResult %= mod
        kResult *= ((k-i) % mod)
        kResult %= mod
        # find inverse to K!
    kResult = find(kResult)
    return (nResult * kResult) % mod
sys.stdout.write(str(getResult(N, K)) + "\n")


