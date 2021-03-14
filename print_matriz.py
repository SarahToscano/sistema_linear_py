def print_matriz(matriz, row, column):
    for i in range (0, row):
        for k in range (0, column):
            if(k!=row):
                print (round(matriz[i][k],2), " ", end="")
            else:
                print ("|", round(matriz[i][k],2))
    print("\n")