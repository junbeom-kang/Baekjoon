import sys
input = sys.stdin.readline
n=int(input())
palin=list(input().strip())

for i in range(n//2):
    if palin[i]==palin[-(i+1)]:
        if palin[i]=='?':
            palin[i]='a'
            palin[-(i + 1)]='a'
    else:
        if palin[i]=='?':
            palin[i]=palin[-(i+1)]
        else:
            palin[-(i+1)]=palin[i]
if n%2:
    if palin[n//2]=='?':
        palin[n//2]='a'
for i in palin:
    print(i,end='')