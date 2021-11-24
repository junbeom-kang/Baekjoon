import sys
input=sys.stdin.readline

def solution():
    def get(z):
        if z == 'B':
            s1, s2 = 0, score['B']
        elif z == 'S':
            s1, s2 = score['B'], score['S']
        elif z == 'G':
            s1, s2 = score['S'], score['G']
        elif z == 'P':
            s1, s2 = score['G'], score['P']
        else:
            s1, s2 = score['P'], score['D']
        return s1,s2
    n=int(input())
    s,g,p,d=map(int,input().split())
    r = input().rstrip()
    score={'B':s,'S':g,'G':p,'P':d,'D':d+1}
    dp=[[0]*501 for _ in range(n)]
    s1,s2=get(r[0])
    for i in range(s1,s2):
        dp[0][i]=i
    for i in range(1,n):
        for j in range(score[r[i]]):
            s1,s2=get(r[i])
            if r[i]=='D':
                for t in range(s1 - j, s2):
                    if dp[i - 1][t]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][t] + j)
            else:
                for t in range(s1-j,s2-j):
                    if t>=0:
                        dp[i][j]=max(dp[i][j],dp[i-1][t]+j)
    print(max(dp[n-1]))
    return

if __name__ == '__main__':
    solution()

