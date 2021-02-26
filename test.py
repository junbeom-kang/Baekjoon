import sys
input=sys.stdin.readline
def main():
    a,b=0,0
    x = input().rstrip()
    for i in x:
        if i=='(':
            a+=1
        else:
            b+=1
    if a==b:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()