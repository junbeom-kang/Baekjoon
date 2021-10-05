import sys
input=sys.stdin.readline

def solution(arr):
    global cnt,can
    def go(x,y):
        global cnt,can
        if y==m-1:
            cnt+=1
            can=False
            return
        if x-1>=0 and arr[x-1][y+1]=='.':
            arr[x-1][y+1]='x'
            go(x-1,y+1)
        if can and arr[x][y+1]=='.':
            arr[x][y+1]='x'
            go(x,y+1)
        if can and x+1<=n-1 and arr[x+1][y+1]=='.':
            arr[x+1][y+1]='x'
            go(x+1,y+1)
    cnt=0
    for i in range(n):
        can=True
        if arr[i][0]=='.':
            go(i,0)
    print(cnt)
    return

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(input().rstrip()))
    solution(arr)
