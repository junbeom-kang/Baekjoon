n=int(input('숫자를 입력하시오 '))
ans=0
for i in range(1,n+1):
    if i%2==1:
        ans=ans+i
print('1부터 입력한숫자까지 홀수의 총합',ans)