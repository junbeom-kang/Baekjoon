import sys
from math import gcd
input=sys.stdin.readline
def makeTable(string):
    table=[0]*n
    i=0
    for j in range(1,n):
        while i>0 and string[i]!=string[j]:
            i=table[i-1]
        if string[i]==string[j]:
            i+=1
            table[j]=i
    return table
def KMP(string):
    string*=2
    i=0
    ans=0
    for j in range(1,2*n):
        while i>0 and find[i]!=string[j]:
            i=table[i-1]
        if find[i]==string[j]:
            if i==n-1:
                i=table[i]
                ans+=1
            else:
                i+=1
    return ans



n=int(input())
find=input().split()
string=input().split()
table=makeTable(find)
temp=KMP(string)
g=gcd(temp,n)
print('{}/{}'.format(temp//g,n//g))
