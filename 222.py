import sys
from itertools import combinations
input=sys.stdin.readline

a=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
dic={}
for x in a:
    x=list(x)
    x.sort()
    for y in course:
        for z in combinations(x,y):
            print(z)
            if z in dic:
                dic[z]=1
            else:
                dic[z]=0
print(dic)


def solution(orders, course):
    #for
    answer = []
    return answer