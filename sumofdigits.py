def sumofdigits(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
num=int(input("Enter the value of n:"))
print("Sum of digits: ",sumofdigits(num))