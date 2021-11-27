from collections import defaultdict
def solution(source):
    dic=defaultdict(int)
    n=len(source)
    answer=""
    sum=n
    for i in range(n):
        dic[source[i]] += 1
    while sum>0:
        for i in range(97,123):
            if dic[chr(i)]>0:
                answer+=chr(i)
                dic[chr(i)]-=1
                sum-=1
    print(answer)
    return answer








if __name__ == '__main__':
    solution("")