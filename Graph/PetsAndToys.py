import sys
input=sys.stdin.readline

def solution(P, T, A, B):
    l=len(P)
    m=len(A)
    adj=[[]for _ in range(l)]
    for i in range(m):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    visited=[False]*l

    for i in range(l):
        if not visited[i]:
            visited[i]=True
            up=P[i]
            down=T[i]
            q=[i]
            while q:
                v=q.pop()
                for e in adj[v]:
                    if not visited[e]:
                        visited[e]=True
                        up+=P[e]
                        down+=T[e]
                        q.append(e)
            if up!=down:
                return False

    return True

if __name__ == '__main__':
    print(solution([2, 2, 1, 1, 1],[1, 1, 1, 2, 2],[0, 1, 2, 3],[1, 2, 0, 4]))

