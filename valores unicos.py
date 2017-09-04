def valoresUnicos(string):
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if(string[i]==string[j] and j>i):
                return True
cadena=str(input("Introduzca la cadena: "))
if(valoresUnicos(cadena)==True):
    print("La cadena no tiene valores unicos")
else:
    print("La cadena tiene valores unicos")
