import sys
input=sys.stdin.readline
def search(text):
    cur=trie
    for i in text:
        cur=cur[i]
    print('%s %.4f'%(cur['*'][0],cur['*'][1]/L*100))

text=[]
while True:
    temp=input().rstrip()
    if temp=='':
        break
    text.append(temp)
text.sort()
L=len(text)
trie={}
for i in text:
    cur = trie
    for char in i:
        if char not in cur:
            cur[char]={}
        cur=cur[char]
    if '*' not in cur.keys():
        cur['*']=[i,1]
    else:
        cur['*'][1]+=1
temp=set(text)
temp=list(temp)
temp.sort()
for i in temp:
    search(i)