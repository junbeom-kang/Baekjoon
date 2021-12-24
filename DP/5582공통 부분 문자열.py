import sys
input=sys.stdin.readline

def solution(s,t):
    n=len(s)
    m=len(t)
    arr=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
    print(max(map(max, arr)))
    return

if __name__ == '__main__':
    s=input().rstrip()
    t=input().rstrip()
    solution(s,t)

