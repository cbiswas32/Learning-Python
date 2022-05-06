from tkinter.tix import COLUMN


row=8
column=8

for i in range(row):
    for j in range(column):
        if(i==0 or i== row-1 or j==0 or j== column-1):
            print("*", end='')
        else:
            print(" ", end='')
    print()            


