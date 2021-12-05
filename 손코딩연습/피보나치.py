#재귀로 피보나치 구현하기
def fibonacirecur(v):
    print(v)
    if v<=1:
        return v
    else:
        return fibonacirecur(v-1)+fibonacirecur(v-2)

def fibonacimemo(n):
    if n>0:
        memo=[0]*(n+1)
        memo[1]=1
        for i in range(2,n+1):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[n]
    else:
        return 0
def fact(v):
    if v==1:
        return v
    else:
        return fact(v-1)*v

#print(fibonacirecur(int(input()))
#print(fibonacimemo(int(input())))
print(fact(3))