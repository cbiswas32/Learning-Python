def raplceWordStrip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()


this="   Harry is good   "
print(raplceWordStrip(this,"is"))
#print(this)
#print(this.strip())
#Strip  removes unwanted the spaces from a string
