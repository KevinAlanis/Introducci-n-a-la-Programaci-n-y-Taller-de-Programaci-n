def formarLista(num):
    if isinstance(num, int)and(num>0):
        return formarLista_aux(num)
    else:
        return "Error, ingrese un número entero positivo"

def formarLista_aux(num):
    if (num==0):
        return []
    if((num%10)%2==0):
        return [num%10]+formarLista_aux(num//10)
    else:
        return formarLista_aux(num//10)
