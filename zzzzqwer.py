import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('C:/nba.csv',delimiter=',')
#1번
temp=df.groupby(['Position','Team'])[['Age','Salary']].mean()
temp
#2번
f=lambda x:x.max()
gp_by_pos=df.groupby('Position')
plt.bar(gp_by_pos.apply(f)['Salary'].index,gp_by_pos.apply(f)['Salary'])

#3번
plt.figure(figsize=(18,6))
plt.subplot(2,1,1)
gp_by_team=df.groupby('Team')
change=list(gp_by_team['Salary'].apply(f).index)
for i in range(len(change)):
    a=change[i].split(' ')
    b=a[0][0]+a[1][0]
    change[i]=b
plt.title('Maxium salary for each tem')
plt.bar(change,gp_by_team['Salary'].apply(f))
plt.subplot(2,1,2)
plt.title('Maxium age for each tem')
plt.bar(change,gp_by_team['Age'].apply(f))



