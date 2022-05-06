a=int(input("1st Number: "))
b=int(input("2nd Number: "))
c=int(input("3rd Number: "))

def gratest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the gratest")
    elif(b>a and b>c):
        print(f"{b} is the gratest")
    else:
        print(f"{c} is the gratest")


gratest(a,b,c)

def great(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else: 
        if(n2>n3):
            return n2
        else:
            return n3       

print("Maximum number is",great(10,15,12))