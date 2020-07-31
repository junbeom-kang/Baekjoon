import sys
input=sys.stdin.readline
stack=[]
n,p,e=map(int,input().split())
for _ in range(n):
    stack.append(list(map(int,input().split())))

def backtracking(i,sum,count):
    if e-sum<stack[i][0] and i<len(stack)-1:
        print(i+1,sum,count,'!')
        backtracking(i + 1, sum, count)
    else:
        print(i,sum,count)
        for j in range(stack[i][0],stack[i][1]+1):
            if sum+j==e and count+1==p:
                ans[i]=j
                print(*ans)
                sys.exit()
            elif count+1<p and sum+j<e and i<len(stack)-1:
                ans[i]=j
                backtracking(i+1,sum+j,count+1)

for i in range(len(stack)):
    ans = [0 for _ in range(n)]
    sum=0
    count=0
    backtracking(i,sum,count)
print(-1)
