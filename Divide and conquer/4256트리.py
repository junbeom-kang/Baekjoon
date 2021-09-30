import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution(n,pre_visit,in_visit):
    answer=[]
    def divide(root,left,right,temp):
        if left>right:
            return
        mid=index[root]
        L=mid-left
        R=right-mid
        if temp+1<n:
            divide(pre_visit[temp+1],left,mid-1,temp+1)
        if L+temp+1<n:
            divide(pre_visit[L+temp+1],mid+1,right,temp+L+1)
        answer.append(root)
    start=pre_visit[0]
    divide(start,0,n-1,0)
    return answer

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        n=int(input())
        index=[0]*(n+1)
        pre_visit=list(map(int,input().split()))
        in_visit=list(map(int,input().split()))
        for i in range(n):
            index[in_visit[i]]=i
        print(*solution(n,pre_visit,in_visit))