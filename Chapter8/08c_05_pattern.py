def pattern(x):
    for row in range(x,-1,-1):
        for column in range(0,row):
            print("*", end="")
        print()    

pattern(5)