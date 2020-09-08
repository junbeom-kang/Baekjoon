import sys
input=sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
s.sort()
num = 0
for i in range(n):
    if num+1 < s[i]:
        break
    num += s[i]
print(num+1)