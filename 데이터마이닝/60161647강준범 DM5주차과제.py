import matplotlib.pyplot as plt
import numpy as np

def solve1(score):
    plt.scatter(score[:,1],score[:,0],marker='^')
    plt.xlabel('English')
    plt.ylabel("Korea")
    plt.show()

def solve2(score,subject):
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.hist(score[:,i])
        plt.xlabel(subject[i])
        plt.ylabel('Count')
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    #plt.tight_layout()
    plt.show()

def solve3(score):
    arr=[0]*(4)
    temp=np.where(score[:,0] >= 90, 'A', np.where(score[:,0] >= 80, 'B', np.where(score[:,0] >= 70, 'C', 'D')))
    for i in temp:
        if i=='A':
            arr[0]+=1
        elif i=='B':
            arr[1]+=1
        elif i=='C':
            arr[2]+=1
        else:
            arr[3]+=1
    label = ['A','B','C','D']
    plt.pie(arr, labels=label)
    plt.show()

def solve4(score,subject):
    fig1, ax = plt.subplots()
    ax.boxplot([score[:,0],score[:,1],score[:,2],score[:,3]])
    ax.set_xticklabels(subject)
    plt.ylim(0,100)
    plt.show()

if __name__=="__main__":
    Score = np.random.randint(100, size=(10, 4))
    subject=['Korea','English','Math','Science']
    solve1(Score)
    solve2(Score,subject)
    solve3(Score)
    solve4(Score,subject)