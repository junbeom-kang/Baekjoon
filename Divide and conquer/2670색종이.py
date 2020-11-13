import sys
input=sys.stdin.readline
n=int(input())
adj=[list(map(int,input().split()))for _ in range(n)]
white=0
blue=0
def check(n,x,y):
    temp=adj[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if adj[i][j]!=temp:
                return False,-1
    return True,temp

def divide(n,x,y):
    global white,blue
    a,b=check(n,x,y)
    if a:
        if b==0:
            white+=1
        elif b==1:
            blue+=1
    else:
        divide(n//2,x,y)
        divide(n//2,x+n//2,y)
        divide(n//2,x,y+n//2)
        divide(n//2,x+n//2,y+n//2)

divide(n,0,0)
print(white)
print(blue)