import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def solution():
    global cnt
    def check(l):
        global temp,cnt
        def dfs(x,y):
            global temp
            temp+=1
            for t in range(4):
                nx=x+dx[t]
                ny=y+dy[t]
                if 0<=nx<5 and 0<=ny<5 and [nx,ny] in l and not visited[nx][ny]:
                    visited[nx][ny]=True
                    dfs(nx,ny)

        temp=0
        visited=[[False]*5 for _ in range(5)]
        visited[l[0][0]][l[0][1]]=True
        dfs(l[0][0],l[0][1])
        if temp==7:
            cnt+=1

    def go(start,l,q,w):
        if w==4:
            return
        if q+w==7:
            candidate.append(l)
            return
        for i in range(start+1,25):
            if arr[index[i][0]][index[i][1]]=='Y':
                go(i,l+[[index[i][0],index[i][1]]],q,w+1)
            else:
                go(i,l+[[index[i][0],index[i][1]]],q+1,w)
    candidate=[]
    arr=[]
    index=[]
    for _ in range(5):
        arr.append(list(input().rstrip()))
        for __ in range(5):
            index.append([_,__])
    for i in range(19):
        if arr[index[i][0]][index[i][1]]=='Y':
            go(i,[[index[i][0],index[i][1]]],0,1)
        else:
            go(i,[[index[i][0],index[i][1]]],1,0)
    cnt=0
    for i in candidate:
        check(i)
    print(cnt)
    return

if __name__ == '__main__':
    solution()

