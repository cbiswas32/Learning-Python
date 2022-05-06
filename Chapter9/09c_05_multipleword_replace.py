words=["Chinu","Mrinmoy"]

with open('D:/assignments/python/Chapter9/question5.txt') as f:
    c=f.read()
print(c)


for word in words:
    c=c.replace(word,"****")
    with open('D:/assignments/python/Chapter9/question5.txt','w') as f:
        f.write(c)

print(c)

