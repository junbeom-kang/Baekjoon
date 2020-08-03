import sys
input=sys.stdin.readline
n=int(input())
ans=[]
time=[0]*8001
for i in range(n):
    x=int(input())
    ans.append(x)
    if x<0:
        time[x+8001]+=1
    else:
        time[x]+=1
ans.sort()
ans1=[]
for i in range(8001):
    if time[i]>0:
        if i<=4000:
            ans1.append([time[i], i])
        else:
            ans1.append([time[i], i - 8001])

ans1.sort(key= lambda x:(x[0],-x[1]))
def average(ans):
    return round(sum(ans)/n)

def howMany(ans,n):
    if n==1:
        return ans[0][1]
    else:
        if ans[-1][0]==ans[-2][0]:
            return ans[-2][1]
        else:
            return ans[-1][1]

def MiddleNum(ans):
    return ans[n//2]
def range(ans):
    return ans[-1]-ans[0]

print(average(ans))
print(MiddleNum(ans))
print(howMany(ans1,n))
print(range(ans))
