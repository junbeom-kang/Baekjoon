import sys
input=sys.stdin.readline
def ccw(a,b,c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0])

first=list(map(int,input().split()))
second=list(map(int,input().split()))
f1=first[0:2]
f2=first[2:]
s1=second[0:2]
s2=second[2:]
x=ccw(f1,f2,s1)*ccw(f1,f2,s2)
y=ccw(s1,s2,f1)*ccw(s1,s2,f2)
if x==0 and y==0:
    if f1<f2:
        f1,f2=f2,f1
    if s1<s2:
        s1,s2=s2,s1
    if f1>=s2 and f2<=s1: #생각하기 어렵다.
        print(1)
    else:
        print(0)
if x<=0 and y<=0:
    print(1)
else:
    print(0)