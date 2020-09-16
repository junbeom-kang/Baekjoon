import sys
input=sys.stdin.readline
def add(trie,text):
    cur=trie
    for i in text:
        if i not in cur:
            cur[i]={}
        cur=cur[i]
    cur['*']={}
def search(trie,sample):
    cur=trie
    for i in sample:
        if i not in cur:
            return False
        else:
            cur=cur[i]
    if '*' in cur:
        return True
    else:
        return False





def solution(n,m,text,sample):
    trie={}
    cnt=0
    for i in range(n):
        add(trie,text[i])
    for i in range(m):
        if search(trie,sample[i]):
            cnt+=1
    return cnt



n,m=map(int,input().split())
text=[]
sample=[]
for _ in range(n):
    text.append(input().rstrip())
for _ in range(m):
    sample.append(input().rstrip())
print(solution(n,m,text,sample))