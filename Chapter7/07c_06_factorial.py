
#Using While Loop
num=int(input("Enter a Number: "))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(f"factorial is {fact}")  



#Using For Loop

n=int(input("Enter another Number: "))
fact1=1
for i in range(1,n+1):
    fact1=fact1*i
print(f"factorial is {fact1}")  