import sys
from itertools import combinations
input=sys.stdin.readline

def solution(nicks,emails):
    def find(v):
        if parents[v]==v:
            return v
        else:
            parents[v]=find(parents[v])
            return parents[v]

    def merge(a,b):
        q=find(a)
        w=find(b)
        if q!=w:
            if q<=w:
                parents[w]=q
            else:
                parents[q]=w

    def checknick(a,b):
        if len(a)>len(b):
            temp=b
            b=a
            a=temp
        if len(b)-len(a)==0:
            if a==b:
                return True
            else:
                for i in range(len(a)):
                    for j in range(i,len(a)):
                        if a[:i]+a[:i+1]==b[:j]+b[:j+1]:
                            return True
        elif len(b)-len(a)==1:
            for i in range(len(b)):
                if a==b[:i]+b[:i+1]:
                    return True
        elif len(b)-len(a)==2:
            temp=[i for i in range(len(b))]
            for q,w in combinations(temp,2):
                if a==b[:q]+b[q+1:w]+b[w+1:]:
                    return True
        return False
    def checkemail(a,b):
        fa,sa=a.split('@')
        fb,sb=b.split('@')
        if fa==fb:
            return True
        if sa==sb and abs(len(fa)-len(fb))==1:
            if len(fa)>len(fb):
                temp=fb
                fb=fa
                fa=temp
            for i in range(len(fb)):
                if fa==fb[:i]+fb[i+1:]:
                    return True
        return False

    n=len(nicks)
    parents=[i for i in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            if checknick(nicks[i],nicks[j]):
                if checkemail(emails[i],emails[j]):
                    merge(i,j)
    for i in range(n):
        find(i)
    result=len(set(parents))
    print(result)
    return

if __name__ == '__main__':
    """
    solution(["imhero111","moneyman","hero111","imher1111","hro111","moneyman","moneymannn"]
             ,["superman5@abcd.com","batman432@korea.co.kr","superman@abcd.com","supertman5@abcd.com"
                 ,"superman@erty.net","batman42@korea.co.kr","batman432@usa.com"])
    """
    #solution(["99police","99poli44"],["687ufq687@aaa.xx.yyy","87ufq687@aaa.xx.yy"])
    solution(["99polico","99policd"],["687ufq687@aaa.xx.yyy","587ufq687@aaa.xx.yy"])


