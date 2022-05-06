comment="Hey you Listen to me. click this"
spam=False
if("click this" in comment):
    spam=True
elif("buy now" in comment):
    spam=True
elif("subscribe this" in comment):
    spam=True
elif("make a lot of money" in comment):
    spam=True
else:
    spam=False


if(spam):
    print("this comment is spam")
else:
    print("Not Spam")    
