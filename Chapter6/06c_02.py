sub1=int(input("Sub1 Marks: "))
sub2=int(input("Sub2 Marks: "))
sub3=int(input("Sub3 Marks: "))


total=sub1+sub2+sub3

if(sub1<33 or sub2<33 or sub3<33):
    print("Fail")


if((total/3)<40):
    print("Fail Total")

else:
    print("passed1")    
