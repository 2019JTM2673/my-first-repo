#! /usr/bin/python3
#....program to find avg of numbers which you are enttering"
n=int(input("Enter nums you want: "))
numlst= []
for i in range(n):
    #print(i)
    y=int(input())
    numlst.append(y)
print(numlst) 
sum=0   
for j in numlst:
    sum = sum + j
print(sum)
print("avg of numbers is:",sum/len(numlst))
