#선언한 변수들의 크기를 세 보세요. char = 1바이트, int = 4바이트 이런 식으로 세면 됩니다.
# 그러면 count는 10001 * 4바이트 ~= 40000 바이트 ~= 40KB 정도 되고,
# ary는 N이 최대 = 10000000일 때 약 40000000B ~= 40000KB ~= 40MB이므로 메모리를 초과합니다
import sys
input=sys.stdin.readline
n=int(input())
stack=[[0]for _ in range(10001)]
for i in range(n):
    a=int(input())
    stack[a][0]=stack[a][0]+1
for i in range(10001):
    x=stack[i][0]
    for _ in range(x):
        print(i)
