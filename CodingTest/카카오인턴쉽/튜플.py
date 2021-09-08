def solution(s):
    a=set()
    answer = []
    s=s[2:-2]
    split = s.split("},{")
    split.sort(key=len)
    for i in split:
        for j in i.split(","):
            if j not in a:
                a.add(j)
                answer.append(int(j))
    print(answer)
    return answer

if __name__ == '__main__':
    solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")