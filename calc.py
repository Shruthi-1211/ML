
print("Select Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
choice=input("Enter your choice(1/2/3):")
num1=int(input("enter the first number:"))
num2=int(input("Enter the second number:"))

if choice=='1':
    print(num1+num2)
elif choice=='2':
    print(num1-num2)
else:
    print(num1*num2)
