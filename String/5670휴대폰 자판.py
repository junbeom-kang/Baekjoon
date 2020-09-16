import sys
input=sys.stdin.readline
def add(trie,text):
    cur=trie
    for i in text:
        if i not in cur:
            cur[i]={}
        cur=cur[i]
    cur['*']={}
    return

def searchdfs(cur,cnt,ans):
    if cnt!=0 and len(cur)==1 and '*'not in cur.keys():
        for i in cur:
            searchdfs(cur[i],cnt,ans)
    else:
        for i in cur:
            if i=='*':
                ans.append(cnt)
            else:
                searchdfs(cur[i],cnt+1,ans)

def solution(n,text):
    ans=[]
    trie={}
    for i in range(n):
        add(trie,text[i])
    searchdfs(trie,0,ans)
    print('%.2f'%round(sum(ans)/len(ans),2))


while True:
    try:
        n=int(input())
        text=[]
        for _ in range(n):
            text.append(input().rstrip())
        solution(n,text)
    except:
        break