import os
oldname='D:/assignments/python/Chapter9/oldname.txt'
newname='D:/assignments/python/Chapter9/renamed_by_python.txt'

with open(oldname) as f:
    c=f.read()
with open(newname,'w') as f:
    f.write(c)    


os.remove(oldname)    