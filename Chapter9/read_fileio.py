# Use open function to read the content of a file



# f = open('sample.txt','r') #Specify the  file name and mode 'r'
f = open('D:\\assignments\\python\\Chapter9\\sample.txt') #By default the mode is r



#data=f.read() #read the file
#data=f.read(5) #read the first 5 charecter

#reading individual line for file
data=f.readline() # read first line
print(data)

data=f.readline() # read 2nd line
print(data)


data=f.readline() # read 3rd line
print(data)
#We can use readline() multiple times to read the next line

f.close() #closing the file