import sys

def first(v):
    print(v,end='')
    if adj[v][0]!='.':
        first(adj[v][0])
    if adj[v][1]!='.':
        first(adj[v][1])
def mid(v):
    if adj[v][0]!='.':
        mid(adj[v][0])
    print(v,end='')
    if adj[v][1]!='.':
        mid(adj[v][1])
def last(v):
    if adj[v][0]!='.':
        last(adj[v][0])
    if adj[v][1]!='.':
        last(adj[v][1])
    print(v,end='')

n=int(input())
adj={}
for _ in range(n):
    A,B,C=input().split()
    adj[A]=(B,C)
first('A')
print()
mid('A')
print()
last('A')
