import sys
input=sys.stdin.readline
w=[]
for _ in range(3):
    w.append(list(map(int,input().split())))
temp=(w[0][0]*w[1][1]+w[1][0]*w[2][1]+w[2][0]*w[0][1])-(w[0][1]*w[1][0]+w[1][1]*w[2][0]+w[2][1]*w[0][0])
if temp==0:
    print(0)
elif temp<0:
    print(-1)
else:
    print(1)