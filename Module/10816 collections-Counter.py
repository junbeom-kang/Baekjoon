from collections import Counter
##딕셔너리 형태로 반환해줌
_=int(input())
first=list(map(int,input().split()))
_=int(input())
second=list(map(int,input().split()))
S=Counter(first)
for i in second:
    if not S[i]:
        print(0,end=' ')
    else:
        print(S[i],end=' ')