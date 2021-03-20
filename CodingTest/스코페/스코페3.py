import sys
input=sys.stdin.readline
def find(v):
    cnt=0
    for i in range(n-v+1):
        for j in range(n-v+1):
            can=True
            for q in range(i,i+v):
                for w in range(j,j+v):
                    if not arr[q][w]:
                        can=False
                        break
                if not can:
                    break
            if can:
                cnt+=1
    return cnt


n=int(input())
arr=[[] for _ in range(n)]
ans=[]
for i in range(n):
    arr[i]=list(map(int,input().rstrip()))
for i in range(1,n+1):
    temp=find(i)
    if temp==0:
        break
    else:
        ans.append(temp)
print("total: "+str(sum(ans)))
for i in range(len(ans)):
    print("size[%d]: %d"%(i+1,ans[i]))