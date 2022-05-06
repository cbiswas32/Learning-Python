#with open('D:/assignments/python/Chapter9/donkey_file.txt','w') as f:
#    f.write("Hello I am donkey. He is also donkey")



with open('D:/assignments/python/Chapter9/donkey_file.txt','r') as f:
    containt=f.read()
    print(containt)


containt = containt.replace('donkey','#####')

with open('D:/assignments/python/Chapter9/donkey_file.txt','w') as f:
    f.write(containt)