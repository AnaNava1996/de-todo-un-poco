cad1=str(input("Introduzca la cadena: "))
cad=[]
for j in cad1: cad.append(j) #convertir a lista la cadena

string=[]
i=len(cad)-1

while(i!=-1):   #invertir la cadena
    string.append(cad[i])
    i=i-1
print(string)

