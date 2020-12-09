a=([1,2],[4,5])
cnt=1
while cnt!=5:
    a=a[0][:]
    a[0]+=3
    cnt+=1
print(a)