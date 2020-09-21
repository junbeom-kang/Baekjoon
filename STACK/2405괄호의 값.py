import sys
input=sys.stdin.readline
stack=[]
string=input().rstrip()
def solution(string):
    for i in range(len(string)):
        if string[i]=='(':
            stack.append(')')
        elif string[i]=='[':
            stack.append(']')
        else:
            if stack:
                temp=stack.pop()
                if string[i]!=temp:
                    return False
            else:
                return False
    if stack:
        return False
    ans=[]
    for i in range(len(string)):
        if i==len(string)-1:
            ans.append(')')
        else:
            if string[i]=='(':
                ans.append('2*(')
            elif string[i]=='[':
                ans.append('3*(')
            elif string[i]==')' or string[i]==']':
                if string[i+1]=='('or string[i+1]=='[':
                    ans.append(')+')
                else:
                    ans.append(')')
    cnt=0
    for j in range(len(string)-1):
        if string[j]=='('and string[j+1]==')':
            ans.insert(j+cnt+1,1)
            cnt+=1
        elif string[j]=='['and string[j+1]==']':
            ans.insert(j + cnt + 1, 1)
            cnt += 1
    return eval(''.join(map(str,ans)))

temp=solution(string)
if temp:
    print(temp)
else:
    print('0')