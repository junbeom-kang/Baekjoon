import sys
input=sys.stdin.readline
from collections import Counter

def solution(A):
    a=Counter(A)
    temp=[]
    if a['S']:
        temp.append('S'*a['S'])
    if a['M']:
        temp.append('M'*a['M'])
    if a['L']:
        temp.append('L'*a['L'])
    answer=''.join(temp)
    return answer

if __name__ == '__main__':
    solution("SSSML")

