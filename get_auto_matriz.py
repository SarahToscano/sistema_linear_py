from print_matriz import print_matriz

def get_auto_data():
    for i in range (0,3):
        if(i==1):
            print("**** Programa de Resolucao de Sistema Linear ****")
        else:
            print("*************************************************")
    
    row =3
    column =3
    print ("\nSua matriz é do tipo", row, "X", column, )
    column+=1 #Adição da variavel independente

    matriz = [0]*row
    
    for i in range(row):
        matriz[i] = [0] * column

    matriz = [[11,-2,-1,880], [-3,13,-1,0], [-3,-2,29,-2640]]
    #matriz = [[2,3,-1,5], [4,4,-3,3], [2,-3,1,-1]]
    print_matriz(matriz, row, column)
    return (matriz, row, column)

