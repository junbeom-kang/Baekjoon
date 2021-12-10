import sys
input=sys.stdin.readline
def solution():
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v]=find(parent[v])
            return parent[v]
    def merge(a,b):
        q=find(a)
        w=find(b)
        if q!=w:
            if q>w:
                parent[q]=w
                size[w]+=size[q]
                size[q]=size[w]
            else:
                parent[w]=q
                size[q]+=size[w]
                size[w]=size[q]
        print(size[q])


    n,m=map(int,input().split())
    parent=[i for i in range(n+1)]
    size=[0]
    for i in range(n):
        size.append(int(input()))

    for i in range(m):
        t1,t2=map(int,input().split())
        merge(t1,t2)


    return

if __name__ == '__main__':
    solution()

