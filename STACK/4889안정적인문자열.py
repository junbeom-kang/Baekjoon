import sys
input=sys.stdin.readline
time=1
while 1:
    cnt=0
    temp=input().rstrip()
    if temp[0]=='-':
        break
    else:
        stack=[]
        for i in range(len(temp)):
            if temp[i]=='{':
                stack.append('{')
            elif temp[i]=='}':
                if not stack:
                    cnt+=1
                    stack.append('{')
                elif stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append('}')
    print('{}. {}'.format(time,cnt+len(stack)//2))
    time+=1