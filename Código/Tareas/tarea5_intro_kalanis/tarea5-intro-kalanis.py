def busc(x,lista):
    if isinstance(lista, list)and(lista!=[]):
        return buscar(lista,x,len(lista)//2)
    else:
        return "Error"

def buscar(lista,x,mitad):
    if (mitad == 0 or mitad > (len(lista) -1)):
        return False

    elif (lista[mitad]==x):
        return True

    elif (lista[mitad//2]<x):
        return buscar(lista,x,mitad + mitad//2)
    
    elif (lista[mitad//2]>x):
        return buscar(lista,x,mitad - mitad//2)

    
    
    
