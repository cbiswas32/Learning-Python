mydict={
    "pankha":"Fan",
    "dabba":"box",
    "bastu":"item"
}
print("Options are", mydict.keys())
a=input("enter the hindi word \n")

print("The meaning of the word is: ", mydict['a'])
#if the key provided is not in dict it will provide ERROR


#to avoid this-
print("The meaning of the word is: ", mydict.get(a))
