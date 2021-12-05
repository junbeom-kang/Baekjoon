"""
Q. 정수를 입력 받아 3자리 마다 콤마(,) 를 추가하는 함수를 작성하여라.
예를 들어 1234가 입력되면 1,234를 반환하여야 하고 123456789가 입력되면 123,456,789를 반환하여야 한다. 123이 입력되면 123을 반환한다.
"""
import sys
input=sys.stdin.readline

def solution():
    data="1234"
    l=len(data)-1
    answer=""
    cnt=1
    while cnt<l+2:
        answer=data[l-cnt+1]+answer
        if not cnt%3 and cnt!=l+1:
            answer=","+answer
        cnt+=3
    print(answer)
    return

if __name__ == '__main__':
    solution()


