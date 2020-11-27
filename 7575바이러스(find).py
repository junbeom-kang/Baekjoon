import sys
input=sys.stdin.readline

n,k=map(int,input().split())
data=[]
for _ in range(n):
    __=int(input())
    data.append(list(input().split()))

for z in range(len(data[0])-k+1):
    t=data[0][z:z+k]
    for m in range(1,n):
        can=''.join(data[m]).find(''.join(data[0][z:z+k]))
        if can==-1:
            can = ''.join(data[m][::-1]).find(''.join(data[0][z:z + k]))
        if can==-1:
            break
        if m==n-1:
            print('YES')
            sys.exit()
print('NO')