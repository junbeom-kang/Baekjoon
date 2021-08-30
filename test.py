import sys
sys.setrecursionlimit(10**9)
def solution(a):
    global temp
    answer = []
    temp=set()
    go("a",1,temp,1)
    for i in a:
        if i in temp:
            answer.append('true')
        else:
            answer.append("false")
    print(answer[0])
    return answer


def go(s,ant,temp,cnt):
    if cnt>500 or s in temp:
        return
    else:
        temp.add(s)
        go(ant*"b"+s+ant*"b",ant,temp,cnt+(ant*2))
        go(s+"a",ant+1,temp,cnt+1)
        go("a"+s,ant+1,temp,cnt+1)

if __name__ == '__main__':
    solution(["abab","bbaa","bababa","bbbabababbbaa"])
    print(temp)
