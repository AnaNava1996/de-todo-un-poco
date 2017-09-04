cadena=str(input("Introduzca la cadena: "))
string=[]
for k in cadena:
    string.append(k)
print(string)
for i in range(0,len(string)):
    cont=1
    for j in range(0,len(string)):
        if((string[j]==string[i]) and (j>i) and string[j]!=' '):
            cont=cont+1
            string[j]=' '
    if(cont>1):
        print("la letra: '"+string[i]+"' se encuentra "+str(cont)+" veces")
