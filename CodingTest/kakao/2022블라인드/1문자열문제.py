from collections import defaultdict
def solution(id_list, report, k):
    totalbanUser=defaultdict(int)
    banlist=defaultdict(set)
    for i in report:
        report,ban=i.split()
        if ban not in banlist[report]:
            banlist[report].add(ban)
            totalbanUser[ban]+=1

    delete=[]
    for i in totalbanUser.keys():
        if totalbanUser[i]<k:
            delete.append(i)
    for i in delete:
        del totalbanUser[i]
    answer=[]
    for i in id_list:
        temp = 0
        for j in banlist[i]:
            if j in totalbanUser:
                temp+=1
        answer.append(temp)
    return answer

if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))