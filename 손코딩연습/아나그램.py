from collections import defaultdict
str1="abdcq2"
str2="adbcq2"
dic1=defaultdict(int)
dic2=defaultdict(int)

for i in range(len(str1)):
    dic1[str1[i]]+=1
for i in range(len(str2)):
    dic2[str2[i]] += 1
print(dic1,dic2)
print(dic1==dic2)