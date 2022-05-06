def sumn(num):
    if(num==1):
        return 1
    return (num+sumn(num-1))    
       

print(sumn(20))


5+sumn(4)

5+4+sumn(3)
5+4+3+sumn(2)
5+4+3+2+sumn(1)
5+4+3+2+1
