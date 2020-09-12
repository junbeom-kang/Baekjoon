import sys
from collections import deque
input=sys.stdin.readline
def removecomma(id):
    newid=deque([])
    i=0
    while i<len(id):
        newid.append(id[i])
        if id[i]=='.':
            while i<len(id)-1 and id[i+1]=='.':
                i=i+1
        i+=1
    return newid

def long(id):
    newid=[]
    for i in range(15):
        newid.append(id[i])
    return newid

def less(id):
    cnt=len(id)
    while cnt<3:
        id.append(id[-1])
        cnt+=1
def remove_first_endcomma(id):
    while len(id)>0 and id[0]=='.':
        id.popleft()
    while len(id)>0 and id[-1]=='.':
        id.pop()

def solution(id):
    id=id.lower()
    id1=deque([])
    for i in id:
        temp=ord(i)
        if 97<=temp<=122 or  48<=temp<=57 or temp==45 or temp==46 or temp==95:
            id1.append(i)
    id1=removecomma(id1)
    remove_first_endcomma(id1)
    if len(id1)==0:
        id1.append('a')
    if len(id1)>=16:
        id1=long(id1)
        remove_first_endcomma(id1)
    if len(id1)<=2:
        less(id1)
    answer="".join(map(str,id1))
    return answer
new_id=input().rstrip()
#solution(new_id)
