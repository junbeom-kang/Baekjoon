from collections import deque
def first(r1,c1,r2,c2):
    def DFS(x,y,l):
        l.append(arr[x][y])
        if r1<=x+1<=r2 and c1<=y-1<=c2:
            DFS(x+1,y-1,l)
        arr[x][y]=l.popleft()

    for i in range(c1,c2+1):
        l=deque([])
        DFS(r1,i,l)
    for i in range(r1+1,r2+1):
        l = deque([])
        DFS(i,c2,l)

n=3
m=5
arr=[[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
x=0
y=0


for i in range(3):
    print(arr[i])
first(0,0,2,4)
print()
for i in range(3):
    print(arr[i])


