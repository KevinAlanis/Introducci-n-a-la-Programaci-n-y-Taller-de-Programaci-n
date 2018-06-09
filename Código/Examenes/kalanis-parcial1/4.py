def intercambiar(lista):
    if isinstance(lista, list):
        return intercambiar_aux(lista, 0)
    else:
        return "Error, ingrese una lista válida"

def intercambiar_aux(lista, exp):
    if (lista==[]):
        return []
    else:
        return ([lista[1]]*(10**exp))+([lista[0]]*(10**exp))+intercambiar_aux(lista[2:], exp)
