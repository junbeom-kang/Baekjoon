from collections import deque
def add(trie,text):
    cur=trie
    for i in text:
        if i not in cur:
            cur[i]={}
        cur=cur[i]
    cur['*']={}
def postOrder(cur,q):
    for i in cur:
        if i=='*':
            for j in q:
                print(j,end=' ')
            print()
        else:
            q.append(i)
            postOrder(cur[i],q)
            q.pop()


def main():
    n=int(input())
    trie={}
    for i in range(n):
        add(trie,list(input().split()))
    Q=[]
    print(trie)
    postOrder(trie,Q)
    return



if __name__ == "__main__":
    main()