import sys
input=sys.stdin.readline

def solution(n,string):
    L=len(string)
    table=[0]*L
    j=0
    for i in range(1,L):
        while j>0 and string[i]!=string[j]:
            j=table[j-1]
        if string[i]==string[j]:
            j+=1
            table[i]=j
    return print(n-table[L-1])

n=int(input())
string=input().rstrip()
solution(n,string)