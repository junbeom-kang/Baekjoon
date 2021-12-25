import sys
input=sys.stdin.readline

def solution(A):
    global answer,s

    def DFS(v, cnt):
        global answer,s
        end = True
        if v.l and v.l.x not in s:
            end = False
            s.add(v.l.x)
            DFS(v.l, cnt + 1)
            s.remove(v.l.x)
        if v.r and v.r.x not in s:
            end = False
            s.add(v.r.x)
            DFS(v.r, cnt + 1)
            s.remove(v.r.x)
        if end:
            answer = max(answer, cnt)

    answer = 0
    s = set()
    s.add(A.x)
    DFS(A, 1)
    print(answer)
    return answer

if __name__ == '__main__':
    solution()

