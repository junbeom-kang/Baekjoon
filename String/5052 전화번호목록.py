import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def add(trie,text):
    cur=trie
    for i in text:
        if i not in cur:
            cur[i]={}
        cur=cur[i]
    cur['*']={}
def bfs(trie):
    queue=deque([trie])
    while queue:
        cur=queue.popleft()
        if len(cur)>=2 and '*' in cur.keys():
            return False
        else:
            for i in cur:
                queue.append(cur[i])
    return True
def solution(n,text):
    trie={}
    for i in range(n):
        add(trie,text[i])
    if bfs(trie):
        print('YES')
    else:
        print('NO')


T=int(input())
for _ in range(T):
    n=int(input())
    text=[]
    for _ in range(n):
        text.append(input().rstrip())
    solution(n,text)