import sys
input=sys.stdin.readline

def solution(s,t):
    ls=len(s)
    lt=len(t)
    while ls!=lt:
        if t[-1]=='A':
            t.pop()
        else:
            t.pop()
            t=t[::-1]
        lt-=1
    if s==t:
        print(1)
    else:
        print(0)
    return

if __name__ == '__main__':
    s=list(input().rstrip())
    t=list(input().rstrip())
    solution(s,t)

