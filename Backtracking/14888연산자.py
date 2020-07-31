import sys
import itertools
input=sys.stdin.readline
n=int(input())
stack=list(map(int,input().split()))
number=list(map(int,input().split()))
operand=[]
count=1
ans=[]
for i in number:
    for _ in range(i):
        operand.append(count)
    count+=1
for i in set(itertools.permutations(operand,len(operand))):
    sum=stack[0]
    for j in range(len(i)):
        if i[j]==1:
            sum+=stack[j+1]
        elif i[j]==2:
            sum-=stack[j+1]
        elif i[j]==3:
            sum*=stack[j+1]
        else:
            if sum<=0 and stack[j+1]>0:
                sum=(abs(sum)//stack[j+1])*-1
            else:
                sum//=stack[j+1]
    ans.append(sum)
print(max(ans))
print(min(ans))
