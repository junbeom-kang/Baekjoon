import sys
input=sys.stdin.readline

def solution():
    def go(num,sum):
        if sum==n:
            print("YES")
            sys.exit()
        elif sum>n or num==cnt+1:
            return
        else:
            go(num+1,sum+(3**num))
            go(num+1,sum)

    n=int(input())
    cnt=0
    while n>3**cnt:
        cnt+=1
    go(0,0)
    print("NO")
if __name__ == '__main__':
    solution()

