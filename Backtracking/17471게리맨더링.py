import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def solution(n,num,arr):
    def cal(l):
        one,zero=0,0
        for i in range(n):
            if l[i]==1:
                one+=num[i+1]
            else:
                zero+=num[i+1]
        return abs(one-zero)


    def check(l):
        def DFS(v):
            visited[v] = True
            for i in arr[v+1]:
                if not visited[i-1]:
                    if l[v]==l[i-1]:
                        DFS(i-1)
        visited=[False]*n
        DFS(0)
        for i in range(n):
            if not visited[i]:
                DFS(i)
                break
        for i in range(n):
            if not visited[i]:
                return False
        return True



    def go(cnt):
        global answer
        if cnt==n:
            if check(list):
                answer=min(answer,cal(list))
            return
        else:
            list[cnt]+=1
            go(cnt+1)
            list[cnt] -= 1
            go(cnt+1)
    list=[0]*n
    go(0)

if __name__ == '__main__':
    answer=sys.maxsize
    n=int(input())
    num=[0]+list(map(int,input().split()))
    arr=[[]for _ in range(n+1)]
    for i in range(1,n+1):
        temp=list(map(int,input().split()))
        arr[i].extend(temp[1:])
    solution(n,num,arr)
    if answer==sum(num) or answer==sys.maxsize:
        print(-1)
    else:
        print(answer)