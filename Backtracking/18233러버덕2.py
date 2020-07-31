import sys
input=sys.stdin.readline
stack=[]
n,p,e=map(int,input().split())
for _ in range(n):
    stack.append(list(map(int,input().split())))
count=p
answer=[0 for _ in range(n)]
def sharing(ans,min):
    for i in ans:
        answer[i]=stack[i][0]
    rest=e-min
    for i in ans:
        if rest>=stack[i][1]-stack[i][0]:
            answer[i]=stack[i][1]
            rest-=stack[i][1]-stack[i][0]
        elif rest<stack[i][1]-stack[i][0]:
            answer[i]+=rest
            rest=0
        if rest==0:
            print(*answer)
            sys.exit()

def backtracking(min,count,i):
    if min>e or count>p:
        return
    elif min<=e:
        if count==p and sum(max)>=e:
            sharing(ans,min)
        else:
            for j in range(i+1,n):
                max.append(stack[j][1])
                ans.append(j)
                backtracking(min+stack[j][0],count+1,j)
                max.pop()
                ans.pop()

for i in range(n):
    max = [stack[i][1]]
    ans=[i]
    backtracking(stack[i][0],1,i)
print('-1')
