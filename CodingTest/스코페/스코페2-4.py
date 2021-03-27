import sys
input=sys.stdin.readline
def makeTable(P):
    lp=len(P)
    Table=[0]*lp
    i=0
    for j in range(1,lp):
        while i>0 and P[i]!=P[j]:
            i=Table[i-1]
        if P[i]==P[j]:
            i+=1
            Table[j]=i
    return Table
def KMP(P,TT):
    cnt=0
    lp=len(P)
    table=makeTable(P)
    for T in TT:
        lt=len(T)
        if lt<lp:
            continue
        i=0
        for j in range(lt):
            while i>0 and P[i]!=T[j]:
                i=table[i-1]
            if P[i]==T[j]:
                if i==lp-1:
                    cnt+=1
                    break
                else:
                    i+=1
    return cnt

n=int(input())
text=[]
for i in range(n):
    text.append(input().rstrip())
m=int(input())
for i in range(m):
    temp=input().rstrip()
    print(KMP(temp,text))

