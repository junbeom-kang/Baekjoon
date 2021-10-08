import sys
input=sys.stdin.readline

def solution(word,prefix):
    def insert(w):
        cur=trie
        for i in w:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
        cur['*']={}

    def check(w):
        can=True
        cur=trie
        for i in w:
            if i not in cur:
                can=False
                break
            cur=cur[i]
        return can
    answer=0
    trie={}
    for i in range(n):
        insert(word[i])
    for i in range(m):
        if check(prefix[i]):
            answer+=1
    print(answer)



    return

if __name__ == '__main__':
    n,m=map(int,input().split())
    word=[]
    prefix=[]
    for i in range(n):
        word.append(input().rstrip())
    for i in range(m):
        prefix.append(input().rstrip())
    solution(word,prefix)
