lista = [12,15,32,42,55,75,122,132,150,180,200]
for i in lista:
    if(i % 5 == 0):
        if(i > 150):
            break
        print(i)