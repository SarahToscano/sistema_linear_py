from print_matriz import print_matriz
from get_manual_matriz import get_manual_data #Interação com usuario
from get_auto_matriz import get_auto_data     #Dados inseridos diretamente no código
import math

def Voltage():
    #Caso queira interagir com o usuario descomente a linha abaixo e comente a subsequente 
    #matriz, row, column = get_manual_data()
    matriz, row, column = get_auto_data()

    L = [0]*row 
    pivo= [0]*row

    for i in range(row):
        L[i] = [0] * column
        pivo[i] = matriz[i][0]

    for k in range( column):
        L[0][k] = matriz[0][k] #Preenchimento da L0

    for l_antes in range (0, row):
        for l_depois in range (l_antes+1, row):
                #print("Op. LINHA", l_antes+1, "com LINHA ", l_depois+1)
                if(l_antes==0):
                    #print("Pivo (m):", pivo[l_depois], "dividido por" , pivo[l_antes], "=", pivo[l_depois]/pivo[l_antes], "\n" )
                    for k in range (0, column):
                        L[l_depois][k]=matriz[l_depois][k] - ((pivo[l_depois]/pivo[l_antes])*matriz[l_antes][k])
                        #print_matriz(L, row, column)
                else:
                    p=L[l_depois][l_antes]/L[l_antes][l_antes]
                    #print("Pivo (m):", L[l_depois][l_antes], "dividido por" , L[l_antes][l_antes], "=", p, "\n" )
                    for k in range (1, column):
                        L[l_depois][k]=L[l_depois][k] - ( p*L[l_antes][k])
    
    print("Matriz apos solucao retroativa:")
    print_matriz(L, row, column)

    #Solucao Retroativa
    S = [0]*row
    i=row
    k=column
    S[2] = round((L[2][3]/ L[2][2]),2)
    S[1] = round((L[1][3] -(L[1][2]*S[2]))/ (L[1][1] ),2)
    S[0] = round((L[0][3] -(L[0][1]*S[1]) - (L[0][2]*S[2]) ) / (L[0][0] ),2)

    print("Solucao do Sistema:", S)
    return(S)


#solucao()