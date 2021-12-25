import sys
input=sys.stdin.readline

def solution(A):
    l=len(A)
    dp=[0]*l
    dp[0]=A[0]
    for i in range(l):
        for j in range(1,7):
            if i-j<0:
                break
            dp[i]=max(dp[i-j]+A[i],dp[i])
    print(dp[l-1])
    return dp[l-1]

if __name__ == '__main__':
    solution([1, -2, 0, 9, -1, -2])

