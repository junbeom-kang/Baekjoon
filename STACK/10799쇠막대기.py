import sys
A=[]
R=[]
long=[]
stack=sys.stdin.readline().strip()
for i in range(len(stack)):
    if stack[i]==')'and stack[i-1]=='(':
        R.append(i)
        A.pop()
        continue
    if stack[i]=='(':
        A.append(i)
    else:
        long.append([A.pop(),i])
count=len(long)
for i,j in long:
    for k in R:
        if i<k and k<j:
            count+=1
print(count)