class FenwickRUPQ:
    def __init__(self, size):
        self.arr = [0] * (size + 1)

    def update(self, i, j, val):
        while i < len(self.arr): self.arr[i] += val; i |= i + 1
        j += 1

        while j < len(self.arr): self.arr[j] -= val; j |= j + 1

    def get(self, i):
        res = 0
        while i >= 0: res += self.arr[i]; i = (i & (i + 1)) - 1
        return res


input = __import__('sys').stdin.readline
MIS = lambda: map(int, input().split())

n = int(input())
arr = list(MIS())
F = FenwickRUPQ(n)
for QUERY in range(int(input())):
    qtype, *param = MIS()
    if qtype == 1:
        i, j, k = param
        F.update(i - 1, j - 1, k)
    else:
        i = param[0] - 1
        print(F.get(i) + arr[i])