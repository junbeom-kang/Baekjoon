import sys
from collections import deque
input=sys.stdin.readline
INF=sys.maxsize
def main():
    Q=deque([])
    ans=INF
    n,m,e=map(int,input().split())
    arr=list(map(int,input().split()))
    Map=[0]*(arr[-1]+1)
    for i in arr:
        Map[i]=1
    Q.append([e,e,e,0])
    while Q:
        v,left,right,count=Q.popleft()
        if v<=left:
            left=v
        if v>=right:
            right=v
        if count==3:
            ans=min(ans,right-left)
        else:
            if Map[v]==1:
                if 1<v:
                    Q.append((v-1,left,right,count+1))
                if v<arr[-1]:
                    Q.append((v+1,left,right,count+1))
            else:
                if 1 < v:
                    Q.append((v+1,left,right,count))
                if v < arr[-1]:
                    Q.append((v-1,left,right,count))
    print(ans)



if __name__ == "__main__":
    main()