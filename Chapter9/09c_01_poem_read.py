f = open('D:\\assignments\\python\\Chapter9\\poem.txt') 
#By default the mode is r
data=f.read()
print(type(data))
if data.__contains__('twinkle'):
    print("Yes it Contains Twinkle")
else:
    print("No, it does not Contains Twinkle") 