import sys
input=sys.stdin.readline

def solution(text):
    def do(temp):
        while len(temp)>3:
            if temp[-4:]==['P','P','A','P']:
                for i in range(4):
                    temp.pop()
                temp.append('P')
            else:
                break
    n=len(text)
    temp=[]
    for i in range(n):
        temp.append(text[i])
        do(temp)
    if temp==['P']:
        print("PPAP")
    else:
        print("NP")
    return

if __name__ == '__main__':
    text=input().rstrip()
    solution(text)

