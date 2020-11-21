import sys
input=sys.stdin.readline
INF=sys.maxsize


n=int(input())
data=[]
for i in range(n):
    a,b,c=map(int,input().split())
    data.append([a,b,c])
if n>=2:
    big=[[-1]*3 for _ in range(2)]
    big[0]=data[0][:]
    small=[[INF]*3 for _ in range(2)]
    small[0]=data[0][:]

    for i in range(1,n):
        for j in range(3):
            if j==0:
                big[1][j]=data[i][j]+max(big[0][j],big[0][j+1])
                small[1][j]=data[i][j]+min(small[0][j],small[0][j+1])
            elif j==2:
                big[1][j]=data[i][j]+max(big[0][j],big[0][j-1])
                small[1][j]=data[i][j]+min(small[0][j],small[0][j-1])
            else:
                big[1][j]=data[i][j]+max(big[0][j],big[0][j+1],big[0][j-1])
                small[1][j]=data[i][j]+min(small[0][j],small[0][j+1],small[0][j-1])
        big[0]=big[1][:]
        small[0]=small[1][:]

    print(max(big[1]),min(small[1]))
else:
    print(max(data[0]),min(data[0]))