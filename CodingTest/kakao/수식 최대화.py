import sys
import copy
from itertools import permutations
input = sys.stdin.readline

def solution(expression):

    numbers = []
    op = []
    num = ""
    for i in expression:
        if i == '*' or i == '+' or i == '-':
            numbers.append(num)
            op.append(i)
            num=""
        else:
            num += i
    numbers.append(num)
    s1=[]
    a=["+","*","-"]
    for i in permutations(a):
        s1.append(getAnswer(copy.deepcopy(op), copy.deepcopy(numbers),i))
    answer = max(s1)
    return answer

def getAnswer(op,numbers,order):
    i=0
    while i<len(op):
        if op[i]==order[0]:
            temp=eval(str(numbers[i])+op[i]+str(numbers[i+1]))
            numbers.pop(i+1)
            numbers[i]=temp
            op.pop(i)
        else:
            i+=1
    i=0
    while i < len(op):
        if op[i] == order[1]:
            temp = eval(str(numbers[i]) + op[i] + str(numbers[i + 1]))
            numbers.pop(i + 1)
            numbers[i] = temp
            op.pop(i)
        else:
            i += 1
    i=0
    while i < len(op):
        if op[i] == order[2]:
            temp = eval(str(numbers[i]) + op[i] + str(numbers[i + 1]))
            numbers.pop(i + 1)
            numbers[i] = temp
            op.pop(i)
        else:
            i += 1
    return abs(numbers[0])





if __name__ == '__main__':
    print(solution("50*6-3*2"))
