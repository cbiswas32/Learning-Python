s=set()
s.add(4)
s.add(5)

# we cant add  List or Dictionary in a set
# because they are not hashable 
    #List are mutable in their life-span 
#It only stores unique value   
 

s.add((6,7))
#  We can add tuple in a set
 




print(s)
print(len(s))

#Removal of an Item
s.remove(4) #remove 4 from the set
#if some value is not in the set it will provide Error

print(s)

print(s.pop())
#removes a random/arbitary value from set and return it

a={1,2,3,4,5,6}
b={6,7,8,9}

print(a.union(b))
print(a.intersection(b))