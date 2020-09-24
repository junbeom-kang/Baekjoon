import numpy as np


def solve1(score):
    temp = np.where(score >= 90, 'A', np.where(score >= 80, 'B', np.where(score >= 70, 'C', 'D')))
    print(temp)
    return


def solve2(score):
    temp=np.mean(score,axis=0)
    print(score[:][:]-temp[:])
    return temp


def solve3(score):
    temp=np.sum(score,axis=1)
    temp=temp.reshape(10,1)
    ans=np.concatenate((score,temp),axis=1)
    print(ans)
    return ans


def solve4(score,mean):
    temp=np.mean(score[:,:4],axis=1).reshape(10,1)   #맨 오른쪽에 넣을 평균을 구함
    average_mean=np.mean(temp)                       #평균의 평균을 구함
    sum_sum=np.sum(score[:,4])                       #총합의 총합을 구함
    score=np.concatenate((score,temp),axis=1)        #10*5배열에 평균을 넣어서 10*6 만듬
    temp1=np.array([sum_sum,average_mean])           #np배열로 만듬
    last=np.concatenate((mean,temp1)).reshape(1,6)   #solve2에서 구했던 국영수과의 평균과 총합의총합,평균의 평균을 배열로만듬
    new=np.concatenate((score,last),axis=0)          #10*6배열과 1*6배열을 합침
    print(new)
    return


if __name__=="__main__":
    Score = np.random.randint(100, size=(10, 4))
    solve1(Score)
    mean=solve2(Score)
    solve3_array=solve3(Score)
    solve4(solve3_array,mean)

