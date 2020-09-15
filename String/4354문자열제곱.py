import sys
input=sys.stdin.readline


def solve(string):
    LS=len(string)
    table=[0]*LS
    j=0
    for i in range(1,LS):
        while j>0 and string[i]!=string[j]:
                j=table[j-1]
        if string[i]==string[j]:
            j+=1
            table[i]=j
    temp=LS-table[LS-1]
    if LS%temp==0:
        return print(LS//temp)
    else:
        return print(1)

while 1:
    temp=input().rstrip()
    if temp=='.':
        break
    else:
        solve(temp)