#Important Question
myDict={
    "chinmoy" : "A Leraner"
}

print(myDict.get("chinmoy"))
print(myDict["chinmoy"])

#If the key is in the Dictionary this will provide same result

print(myDict.get("chinmoy22"))
#if the value is not in the Dictionary the get() method will return None
print(myDict["chinmoy22"])
#but this will provide error as chinmoy22 is not in the dictionary



#to aoid Key error we use get Method
# 
# 


