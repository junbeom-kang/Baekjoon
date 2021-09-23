import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution(n,m,arr):
    def DFS(v,cnt):
        score[v]=cnt
        ret=score[v]
        child=0
        for i in arr[v]:
            if score[i]:
                ret=min(ret,score[i])
            else:
                child += 1
                findRet=DFS(i,cnt+1)
                if cnt!=1 and findRet>=score[v]:
                    answer.add(v)
                ret=min(ret,findRet)

        if cnt==1 and child>=2:
            answer.add(v)
        return ret
    for i in range(1,n+1):
        if not score[i]:
            DFS(i,1)
    print(len(answer))
    for i in sorted(answer):
        print(i,end=' ')


if __name__ == '__main__':
    answer=set()
    n,m=map(int,input().split())
    score=[0]*(n+1)
    arr=[[] for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    solution(n,m,arr)