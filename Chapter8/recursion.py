
def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)    

f= fact(4)
print(f)