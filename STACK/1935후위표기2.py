import sys
def input():
    return sys.stdin.readline()
n=int(input())
data=list(input().strip())
num=[0]*30
stack=[]
for i in range(n):
    num[i]=int(input())
for i in data:
    if 'A'<=i<='Z':
        stack.append(num[ord(i)-ord('A')])
    elif i=='+':
        temp=stack.pop()+stack.pop()
        stack.append(temp)
    elif i=='-':
        temp=stack.pop()
        temp1=stack.pop()-temp
        stack.append(temp1)
    elif i=='*':
        temp=stack.pop()*stack.pop()
        stack.append(temp)
    elif i=='/':
        temp=stack.pop()
        temp1=stack.pop()/temp
        stack.append(temp1)
print('%.2f' %stack[0])
