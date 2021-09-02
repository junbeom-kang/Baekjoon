#서로 다른 두 방 사이에 직접 연결된 길이 여러 개 존재할 수도 있습니다.
import sys

answer = sys.maxsize

def solution(n, start, end, roads, traps):
    global first,second,t,visited
    t=set(traps)
    first=[[]for _ in range(n+1)]
    second=[[]for _ in range(n+1)]
    visited=[[False]*2 for _ in range(n+1)]
    for a,b,c in roads:
        first[a].append((b,c))
        second[b].append((a,c))
    visited[start][0]=True
    DFS(start,end,True,0)
    return answer
def DFS(v,end,status,sum):
    print(v,status,visited)
    global answer
    if v==end:
        print(answer)
        answer=min(answer,sum)
        return
    else:
        if status:
            for b,c in first[v]:
                if not visited[b][0]:
                    if b in t:
                        visited[b][0]=True
                        DFS(b,end,not status,sum+c)
                        visited[b][0]=False

                    else:
                        visited[b][0]=True
                        DFS(b,end,status,sum+c)
                        visited[b][0]=False
        else:
            for b,c in second[v]:
                if not visited[b][1]:
                    if b in t:
                        visited[b][1]=True
                        DFS(b,end,not status,sum+c)
                        visited[b][1]=False
                    else:
                        visited[b][1]=True
                        DFS(b,end,status,sum+c)
                        visited[b][1]=False






if __name__ == '__main__':
    print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],	[2, 3]))



