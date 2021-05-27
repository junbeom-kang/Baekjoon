import sys
input=sys.stdin.readline
ans=[]
text=input().rstrip()
bomb=input().rstrip()
L=len(bomb)
for i in range(len(text)):
    ans.append(text[i])
    print(ans)
    if ans[-1]==bomb[-1]:
        can=True
        cnt=1
        while can and cnt<L-1:
            if ans[-(1+cnt)]!=bomb[-(1+cnt)]:
                can=False
                break
        if can:
            for i in range(L):
                ans.pop()
if not ans:
    print("FRULA")
else:
    print(*ans)