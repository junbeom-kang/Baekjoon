import numpy as np
import random


def solve1(score):
    print("<<<수학점수만 출력>>>")
    print(score[:,2])


def solve2(score):
    ans=[]
    for i in range(10):
        ans.append(sum(score[i,:]))
    print("<<<각 학생의 총 합 점수>>>")
    print(ans)


def solve3(score):
    temp=[True,False,False,False,True,False,True,False,True,True]
    print("<<<1,5,7,9,10 번째의 학생>>>")
    print(score[temp])


def solve4(score):
    print("<<<행과 열 변경>>>")
    print(score.T)
    #print(score.transpose((1,0)))


if __name__=="__main__":
    Score = np.random.randint(100, size=(10, 4))
    #print(Score)
    solve1(Score)
    solve2(Score)
    solve3(Score)
    solve4(Score)
