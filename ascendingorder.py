numbers=[5,15,30,10,25,20]
n=len(numbers)
for i in range(n):
    for j in range(0,n-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print("The Sorted List is:",numbers)