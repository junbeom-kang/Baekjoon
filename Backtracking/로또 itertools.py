import sys
from itertools import combinations
input=sys.stdin.readline
flag=True
while flag:
    line=list(map(int,input().split()))
    n=line.pop(0)
    if n==0:
        sys.exit()
    for i in combinations(line,6):
        print(i)
        print(' '.join(map(str,i)))
    print()





