import sys
def dfs(cur,cnt):
    for i in cur:
        print("{0}{1}".format(cnt*'--',i))
        dfs(cur[i],cnt+1)

input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    temp=list(input().split())
    arr.append(temp[1:])
arr.sort()
trie={}
for i in arr:
    cur=trie
    for char in i:
        if char not in cur:
            cur[char]={}
        cur=cur[char]
dfs(trie,0)

