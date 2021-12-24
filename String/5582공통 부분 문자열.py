import sys
input=sys.stdin.readline

def solution(s,t):
    def do(v):
        for i in range(st-v):
            for j in range(sl-v):
                #print(t[i:i+v+1],s[j:j+v+1])
                if t[i:i+v+1]==s[j:j+v+1]:
                    return True
        return False

    sl=len(s)
    st=len(t)
    temp=min(sl,st)
    left=0
    right=temp-1
    answer=0
    while left<=right:
        mid=(left+right)//2
        print(mid)
        if do(mid):
            left=mid+1
            answer=mid
        else:
            right=mid-1
    print(answer)
    return answer

if __name__ == '__main__':
    s=input().rstrip()
    t=input().rstrip()
    solution(s,t)

