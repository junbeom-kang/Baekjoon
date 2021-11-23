import sys
input=sys.stdin.readline

def solution():
    n=int(input())
    s,g,p,d=map(int,input().split())
    r = input()
    score={'B':s,'S':g,'G':p,'P':d,'D':d+1}
    sum=score[r[0]]-1
    first=sum
    second=0
    for i in range(1,n):
        if r[i]=='D':
            if i==n-1:
                sum+=d
            else:
                second=score[r[i+1]]-1
                sum+=second
        else:
            second=score[r[i]]-first-1
            sum+=second
            first=second
    print(sum)
    return

if __name__ == '__main__':
    solution()

