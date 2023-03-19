#double dice
import random as r
import numpy as np
import matplotlib.pyplot as plt
num=100000 #should be no lower than 100,000
Max=20 #max number of dice sides
y6=[]
y5=[]
y4=[]
y3=[]
y2=[]
y_norm=[]
progress=0
for i in range(1,Max+1): #dice of sides 1-whatever
    progress+=1
    print(progress,"/",Max)
    score2=[]
    score3=[]
    score4=[]
    score5=[]
    score6=[]
    norm_score=[]
    for j in range(num):
        List=[]
        roll1=r.randint(1,i)
        roll2=r.randint(1,i)
        roll3=r.randint(1,i)
        roll4=r.randint(1,i)
        roll5=r.randint(1,i)
        roll6=r.randint(1,i)
        
        List.append(roll1)
        norm_score.append(max(List))
        
        List.append(roll2)
        score2.append(max(List))
        
        List.append(roll3)
        score3.append(max(List))
        
        List.append(roll4)
        score4.append(max(List))
        
        List.append(roll5)
        score5.append(max(List))
        
        List.append(roll6)
        score6.append(max(List))
        
        
    y2.append(np.mean(score2))
    y3.append(np.mean(score3))
    y4.append(np.mean(score4))
    y5.append(np.mean(score5))
    y6.append(np.mean(score6))
    y_norm.append(np.mean(norm_score))
x=np.linspace(1,len(y2),len(y2))

plt.plot(x,y6,linewidth=0.8,label="6 throws")
plt.plot(x,y5,linewidth=0.8,label="5 throws")
plt.plot(x,y4,linewidth=0.8,label="4 throws")
plt.plot(x,y3,linewidth=0.8,label="3 throws")
plt.plot(x,y2,linewidth=0.8,label="2 throws")
plt.plot(x,y_norm,linewidth=0.8,label="1 throw")
plt.plot(x,x,linewidth=0.8,label="infinite throws",c='k')

print(y_norm)

plt.grid()
plt.legend()
plt.xticks(x)
plt.yticks(x)

plt.xlabel("number of sides of dice")
plt.ylabel("highest expected number ")