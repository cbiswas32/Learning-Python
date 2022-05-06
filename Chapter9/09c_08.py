with open('D:/assignments/python/Chapter9/this.txt') as f:
    c=f.read()
    
with open('D:/assignments/python/Chapter9/copy.txt','w') as f:
    f.write(c)
    
    f.write("\nthis is copy")
