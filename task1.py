f=input('input path') #input file
a=open(f,'r') #open file into a
l=[]
for i in a:
    x=float(i)
    l.append(x)
l.sort() # sort list
n=len(l) # к-во элементов
#вычисляем 90 персентиль
jmin=int((n*0.9)//1)-1
jmax=jmin+1
jx=(n*0.9)%1
P=l[jmin]+(l[jmax]-l[jmin])*jx
print(round(P,2))#print perc90
#вычисляем медиану
if n%2==0:
    M=(l[int(n/2-1)]+l[int(n/2)])/2
else:
    M=l[int(n/2)]
print(round(M,2)) #печать медианы
print(round(l[n-1],2)) #максимальное значение     
print(round(l[0],2)) # минимальное значение
s=0
for i in l:
    s=s+i
print(round(s/n,2)) #среднее
    
