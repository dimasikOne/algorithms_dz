from array import *

print("Enter some nums for array to sort")
print("print '0' to stop ")

data=int(input())
mas=array('i', [data])
i=1
while mas[i-1]!=0:
    mas.insert(i,int(input()))
    i=i+1
print("Before:")
print(mas)
for i in range(int(len(mas)/2)):
    temp=mas[i]
    mas[i]=mas[len(mas)-i-1]
    mas[len(mas) - i-1]=temp
print("After:")
print(mas)