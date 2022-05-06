def game():
    return 64

score=game()

with open('D:\\assignments\\python\\Chapter9\\hiscore.txt') as f:
    hiscoreStr=f.read()



if hiscoreStr=='':
     with open('D:\\assignments\\python\\Chapter9\\hiscore.txt','w') as f1:
        hiscore=f1.write(str(score))


elif int(hiscoreStr)<score:
    with open('D:\\assignments\\python\\Chapter9\\hiscore.txt','w') as f1:
        hiscore=f1.write(str(score))
