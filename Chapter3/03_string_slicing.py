greeting="good morning! "
name="Chinmoy"
#print(type(name))

#c=greeting+name
print(greeting+name)
# concatation operation using "  +  " symbol


#slicing operation
sliceit="Chinmoy"
print(sliceit[2])

#sliceit[4]="d"
#String doesnot support charecter assignment

print(sliceit[0:3]) #print 0 th 1 th 2 nd elemnt 
#not [first:last]
#starts from first 
#ends at last-1


#print(sliceit[:3]) is same as print(sliceit[0:3])
#print(sliceit[1:]) is same as print(sliceit[1:length(7)])

print(sliceit[0:7:1])#no skip
print(sliceit[0:7:2])#every 2nd value skips