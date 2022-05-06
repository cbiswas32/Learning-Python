n=5
for i in range(n):
    print(" "*(n-i-1),end=" ") 
    # We use end=" " here for avoid new line in printing
    print("*"*(i*2 + 1),end=" ")
    print(" ")
        
