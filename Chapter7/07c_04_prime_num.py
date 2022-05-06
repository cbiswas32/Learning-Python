num=int(input("Plz Enter a Number: "))

#for i in range(2,num):
#    if num%i==0:
#        print("not prime")
#        break
#    else:
#          print("prime")   
#          break
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break   

if prime:
    print("The Number is Prime")
else:
    print("Not Prime")