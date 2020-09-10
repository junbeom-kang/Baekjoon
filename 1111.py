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
print(maketable('abacaaba'))