import random

#create a bubblesort
def bubbleSort(a):
    l=len(a)
    for i in range (0,l):
        cur=i
        for j in range (0,l-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
    

#define a dynamic list
length=(random.randint(1,10))
myList=[]

#entering random numbers in the list
for i in range(length):
    myList.append(random.randint(0,100))
print(f"My initial list: {myList}")
print(f"My list sorted with bubble sort: {bubbleSort(myList)}") 
