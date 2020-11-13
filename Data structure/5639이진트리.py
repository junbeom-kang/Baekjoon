import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
Q=[]
ans=[]
while True:
    try:
        Q.append(int(input()))
    except:
        break
def BS(L,R,root):
    x=L
    if Q[R]>root:
        while L<=R:
            mid=(L+R)//2
            if Q[mid]>root:
                R=mid-1
            else:
                L=mid+1
        if Q[mid]>root:
            return mid
        else:
            return mid+1
    else:
        return x

def divide(left,right):
    if left==right:
        ans.append(Q[left])
        return
    root=Q[left]
    ans.append(root)
    temp=BS(left+1,right,root)
    if temp==left+1:
        divide(temp,right)
        return
    else:
        divide(temp, right)
        divide(left+1,temp-1)
divide(0,len(Q)-1)
for i in ans[::-1]:
    print(i)