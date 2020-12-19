import sys,math
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def re(x):
    global count
    count+=1
    print(x)
    if arr[x]:
        return arr[x]
    temp=int(math.sqrt(x))
    l=[]
    for i in range(1,temp+1):
        l.append(1+re(x-(i**2)))
    arr[x]=min(l)
    return arr[x]
count=1
n=int(input())
arr=[0]*(n+1)
t=int(math.sqrt(n))
for i in range(1,t+1):
    arr[i**2]=1
print(re(n))
print(count)
