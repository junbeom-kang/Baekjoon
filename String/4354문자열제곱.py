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
    j=0
    for i in range(1,LS):
        while j>0 and string[j]!=string[i]:
            j=table[j-1]
        if string[i]==string[j]:
            j+=1
    print(i,j)
    return print(len(string)//(i-j-1))







while 1:
    temp=input().rstrip()
    if temp=='.':
        break
    else:
        solve(temp)