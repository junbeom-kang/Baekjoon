import sys
input=sys.stdin.readline

def makeTable(temp):
    table=[0]*lt
    i=0
    for j in range(1,lt):
        while i>0 and temp[i]!=temp[j]:
            i=table[i-1]
        if temp[i]==temp[j]:
            i+=1
            table[j]=i
    return table

def KMP(string,table,find):
    i=0
    for j in range(len(string)):
        while i>0 and string[j]!=find[i]:
            i=table[i-1]
        if string[j]==find[i]:
            if i==lt-1:
                return 1
            else:
                i+=1
    return 0

string=input().rstrip()
find=input().rstrip()
lt = len(find)
table=makeTable(find)

print(KMP(string,table,find))

