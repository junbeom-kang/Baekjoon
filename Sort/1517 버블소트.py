import sys
input=sys.stdin.readline

def merge(a,b):
    global cnt
    la,lb=len(a),len(b)
    i,j=0,0
    temp=[]
    while i<la and j<lb:
        if a[i]>b[j]:
            temp.append(b[j])
            j+=1
            cnt+=la-i
        else:
            temp.append(a[i])
            i+=1
    if i==la:
        temp.extend(b[j:])
    else:
        temp.extend(a[i:])
    return temp

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    left=0
    right=len(arr)-1
    mid=(left+right)//2
    return merge(merge_sort(arr[left:mid+1]),merge_sort(arr[mid+1:]))

n=int(input())
cnt=0
arr=list(map(int,input().split()))
merge_sort(arr)
print(cnt)