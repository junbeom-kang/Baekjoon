import sys
input=sys.stdin.readline
text=input().rstrip()
pattern=input().rstrip()
ans=[]
temp=-1
while True:
    temp=''.join(text).find(pattern,temp+1)
    if temp==-1:
        break
    ans.append(temp+1)

print(len(ans))
print(*ans)