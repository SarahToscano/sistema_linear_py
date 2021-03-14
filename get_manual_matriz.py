from print_matriz import print_matriz

def get_manual_data():
    for i in range (0,3):
        if(i==1):
            print("**** Programa de Resolucao de Sistema Linear ****")
        else:
            print("*************************************************")
    
    row = input('Quantas linhas tem o sistema?')
    column = input('Quantas colunas tem o sistema?')

    row = int(row)
    column = int(column)

    print ("\nSua matriz é do tipo", row, "X", column, )

    column+=1 #Adição da variavel independente

    matriz = [0]*row
    
    for i in range(row):
        matriz[i] = [0] * column

    print("Insira os dados para preenche-la: ")
    for i in range (0, row):
        print("-- Preenchimento da Linha (", i+1, ")")
        for j in range (0,column):
            if(j==row):#Coluna do termo independete
                matriz[i][j]=input('Digite o termo independete: ')
                print()
            else:
                print("Digite o Coefinciente (", j+1, "): " )
                matriz[i][j]=input()
    
    print_matriz(matriz, row, column)
    return (matriz, row, column)


