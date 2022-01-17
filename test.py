#3자리 단위로 쉼표를 찍자
#7이면 쉼표2개 9자리면 2개 100,000,000 3으로 나누고 ceil 연산이 필요함
#슬라이싱
#01234567

import sys
import math
from collections import deque
input=sys.stdin.readline

def solution(text):
    text=str(text)
    n=len(str(text))
    textlist = []
    t = n % 3
    if t==0:
        t=3
    textlist.extend([text[0:t]])

    cnt=math.ceil(n/3)
    print(cnt)
    for i in range(cnt-1):
        textlist.extend([',',text[t+i*3:t+i*3+3]])
    print(textlist)
    #if n!=cnt*3:
    #    textlist.extend(cnt*3)
    print(''.join(textlist))
    return

if __name__ == '__main__':
    solution(1)

