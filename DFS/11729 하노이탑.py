n=int(input())
cnt=0
ans=[]
def hanoi(n,start,tool,goal):
    global cnt
    if n==1:
        ans.append((start,goal))
        cnt+=1
        return
    hanoi(n-1,start,goal,tool)
    ans.append((start,goal))
    cnt+=1
    hanoi(n-1,tool,start,goal)
hanoi(n,1,2,3)
print(cnt)
for i in ans:
    print(*i)