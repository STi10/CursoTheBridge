lista = [1,2,3,4,5]
for i in range(len(lista)):
    print("\n")
    for i in reversed(lista):
        print(i , end=" " )
    lista.pop()
