from collections import defaultdict


def solution(gems):
    ans=[0,100001]
    glist = set()
    dic = defaultdict(int)
    for i in gems:
        glist.add(i)
    l = len(gems)
    i = 0
    for j in range(l):
        dic[gems[j]] += 1
        if len(dic.keys())==len(glist):
            while len(dic.keys())==len(glist):
                if ans[1] - ans[0] > j - i:
                    ans[1] = j + 1
                    ans[0] = i + 1
                dic[gems[i]] -= 1
                if dic[gems[i]] == 0:
                    del dic[gems[i]]
                i += 1

    return ans


if __name__ == '__main__':
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
