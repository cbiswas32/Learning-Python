from ast import If


num1=int(input("Enter num1: \n"))
num2=int(input("Enter num2: \n"))
num3=int(input("Enter num3: \n"))
num4=int(input("Enter num4: \n"))

if(num1>num2) :
     f1=num1
else:
    f1=num2

if(num3>num4) :
     f2=num3
else:
    f2=num4


if(f1>f2):
    print("gratest is ", f1)
else:
     print("gratest is ", f2)