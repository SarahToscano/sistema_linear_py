from print_matriz import print_matriz
from get_manual_matriz import get_manual_data #Interação com usuario
from get_auto_matriz import get_auto_data     #Dados inseridos diretamente no código
from gauss import Voltage 
import math 

V = Voltage()
I = [0]*6
I[0] = round((110-V[0])/2, 2)   #R1: 110 V1    2
I[1] = round((V[1])/3, 2)       #R2: v2  0     3
I[2] = round((V[2]+110)/2, 2)   #R3: v3 -110   2
I[3] = round((V[0]-V[1])/8, 2)  #R4: v1  v2    8
I[4] = round((V[1]-V[2])/24, 2) #R5: v2  v3    24
I[5] = round((V[0]-V[2])/16, 2) #R6: v1  v3    16
print ("Correntes:", I)