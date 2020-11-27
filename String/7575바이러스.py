import sys
input=sys.stdin.readline
def makeTable(temp):
    table=[0]*k
    i=0
    for j in range(1,k):
        while i>0 and temp[i]!=temp[j]:
            i=table[i-1]
        if temp[i]==temp[j]:
            i+=1
            table[j]=i
    return table

def KMP(string,find,temp):
    i=0
    for j in range(len(string)):
        while i>0 and string[j]!=find[i]:
            i=temp[i-1]
        if string[j]==find[i]:
            if i==k-1:
                return 1
            else:
                i+=1
    return 0

n,k=map(int,input().split())
data=[]
for _ in range(n):
    __=int(input())
    data.append(list(input().split()))

for z in range(len(data[0])-k+1):
    t=makeTable(data[0][z:z+k])
    for m in range(1,n):
        can=KMP(data[m],data[0][z:z+k],t)
        if not can:
            can=KMP(data[m][::-1],data[0][z:z+k],t)
        if not can:
            break
        if m==n-1:
            print('YES')
            sys.exit()
print('NO')




