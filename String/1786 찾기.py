import sys
input=sys.stdin.readline
def maketable(pattern):
    p=len(pattern)
    table=[0]*p
    j=0
    for i in range(1,p):
        while j>0 and pattern[i]!=pattern[j]:
                j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
    return table

def SMP(text,pattern,table):
    ans=[]
    j = 0
    text_len=len(text)
    patter_len=len(pattern)
    for i in range(text_len):
        while j>0 and pattern[j]!=text[i]:
            j=table[j-1]
        if pattern[j]==text[i]:
            if j==patter_len-1:
                ans.append(i-patter_len+2)
                j=table[j]
            else:
                j+=1
    return ans

text=input().rstrip()
pattern=input().rstrip()
table=maketable(pattern)
ans=SMP(text,pattern,table)
print(len(ans))
print(*ans)

