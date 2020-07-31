import sys
input=sys.stdin.readline
zero=[]
adj=[list(map(int,input().split())) for _ in range(9)]


def backtracking(v,start,count):
    if v in temp[start[0]]:
        return
    for i in range(9):
        if temp[i][start[1]]==v:
            return
    x,y=start[0]//3,start[1]//3
    for i in range(3*x,3*x+3):
        for j in range(3*y,3*y+3):
            if temp[i][j]==v:
                return
    temp[start[0]][start[1]]=v
    if count==len(zero)-1:
        for i in range(9):
            print(*temp[i])
        sys.exit()

    for i in range(1,10):
        backtracking(i,zero[count+1],count+1)
    temp[start[0]][start[1]] = 0

for i in range(9):
    for j in range(9):
        if adj[i][j]==0:
            zero.append((i,j))
for i in range(1,10):
    count=0
    temp=adj
    backtracking(i,zero[count],count)