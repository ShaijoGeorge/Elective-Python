print("Select Operator")
print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")
choice=input("Enter Choice (1/2/3/4): ")
n1=float(input("Enter the First Number: "))
n2=float(input("Enter the Second Number: "))
if choice=='1':
    print(n1,"+",n2,"=",n1+n2)
elif choice=='2':
    print(n1,"-",n2,"=",n1-n2)
elif choice=='3':
    print(n1,"*",n2,"=",n1*n2)
elif choice=='4':
    print(n1,"/",n2,"=",n1/n2)
else:
    print("Invalid choice!")