import sys
def input():
    return sys.stdin.readline()
data=[1]
while data[0]!=0:
    data=list(map(int,input().split()))
    len=6
    stack=[]
    temp=0
    size=data[0]
    def DFS(size,temp,len):
        temp+=1
        gap = size - len + 1
        if len==0:
            for i in stack:
                print(i,end=' ')
            print()
            return
        len-=1
        for i in range(gap):
            stack.append(data[temp+i])
            DFS(size-i-1,temp+i,len)
            stack.pop()
    DFS(data[0],temp,len)
    print()
