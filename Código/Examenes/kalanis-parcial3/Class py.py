class Python:
    def __init__(self):
        pass

    def ordenar(self,lista):
        return self.ordenarlista(lista)

    def ordenarlista(self, lista):
        for indice in range(len(lista)):
            if indice==len(lista):
                lista

            elif lista[indice]<lista[indic+1]:
                lista

            elif lista[indice]>lista[indice+1]:
                listaTemp=lista[indice]
                lista[indice]=lista[indice+1]
                liista[indice+1]=listaTemp

            elif lista[indice]<lista[indic+1]:
                lista

            elif lista[indice]>lista[indice+1]:
                listaTemp=lista[indice]
                lista[indice]=lista[indice+1]
                liista[indice+1]=listaTemp

        return lista

    def contar(numero):
        return contardigitos(numero)

    def contardigitos(numero):
        resultado=1
        while (numero!=0):
            numer//10
            resultado+=1

        return resultado

    def multiplicar(matriz1, matriz2):
        return multiplicar_aux(matriz1, matriz2)

    def multiplicar_aux(matriz1,matriz2):
        matriz3=[]
        for fila in range(len(matriz1)):
            contador=0
            matriz3+=[matriz1[fila][contador]*matriz2[contador][fila]]
            contador+=1
            for columna in range(len(matriz2[0])):
                contador2=0
                matriz3+=[matriz1[columna][contador2]*matriz2[contador2][columna]]
                contador2+=1
        return matriz3
        
