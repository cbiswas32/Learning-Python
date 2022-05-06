for i in range(2,20):
    with open(f"D:/assignments/python/Chapter9/tables/MulTableOf{i}.txt",'w') as f:

        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")

  