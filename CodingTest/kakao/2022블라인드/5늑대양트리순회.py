import sys
sys.setrecursionlimit(10**9)
def solution(info, edges):
    global check,needToCheck,mom
    check=[False]*len(info)
    child=[[] for _ in range(len(info))]
    mom=[[]for _ in range(len(info))]
    needToCheck=set()
    for a,b in edges:
        child[a].append(b)
        mom[b].append(a)
    check[0]=True
    start(0,0,0,info,child)
    print(check)
    answer = 0
    return answer

def start(v,sheep,wolf,info,arr):

    check[v]=True
    for i in needToCheck:
        if arr[i]==1:
            if sheep>wolf+1:
                needToCheck.remove(v)
                start(v,sheep,wolf+1,info,arr)
            else:
                needToCheck.add(v)
    for i in arr[v]:
        if info[i]==1:
            if sheep>wolf+1:
                start(v,sheep,wolf+1,info,arr)
        elif info[i]==0:
            start(i,sheep+1,wolf,info,arr)
def checkMother(v):
    temp=v
    check[v] = True
    while temp==0:
        mom[temp]=True
        temp=mom[temp]



#늑대가 많아서 못갔던곳을 list에 넣어놓자
if __name__ == '__main__':
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

