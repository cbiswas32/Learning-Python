c=True
i=1
with open('D:/assignments/python/Chapter9/log.txt') as f:
    while c:

        c=f.readline()
        

        
        if "python" in c.lower():
            print("Yes Python is Prasent! on line no",i)
            print(c)
     
        i+=1


