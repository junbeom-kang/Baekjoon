n=int(input())
v=input()[::2]
print((v*2).find(v,1))
print('1/%s'%(v*2).find(v,1))