myDict={
    "fast": "in a quick manner",
    "chinmoy": "A Learner",
    "marks":[1,2,3,4],
    "dict2":{"name": "chinmoy"},
    1: 2
}


print(list(myDict.keys()))

#Prints the keys of the Dictionary
#We are typecasting(to List) the value of myDict as it is the type of Dict Keys

print(list(myDict.values()))

#Prints the keys of the Dictionary
#We are typecasting(to List) the value of myDict as it is the type of Dict Values


print((myDict.items()))
#all the key, value Pair in the dictionary



#adding contain

updateDict={
    10:20,
    20:40,
    30:90
}

myDict.update(updateDict)

print(myDict)


#Important Question
print(myDict.get("chinmoy"))
print(myDict["chinmoy"])