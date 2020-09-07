import random
def main():
    concatenate()
    calculateGrade()

def concatenate():
    Lst1 = [random.randint(1, 100) for i in range(20)]
    Lst2 = [random.randint(1, 100) for i in range(20)]
    newLst=set(Lst1+Lst2)
    return print(newLst)

def calculateGrade(): #입력값은 각각 띄워서 10개씩 8줄 받도록 하였습니다.
    ans=['D','B','D','C','C','D','A','E','A','D']
    table=[[None]*10 for _ in range(8)]
    for i in range(8):
        table[i]=list(input().split())
    for i in range(8):
        cnt = 0
        for j in range(10):
            if table[i][j]==ans[j]:
                cnt+=1
        print(i,'번 학생의 정답 문항의 개수는',cnt,'입니다')

main()