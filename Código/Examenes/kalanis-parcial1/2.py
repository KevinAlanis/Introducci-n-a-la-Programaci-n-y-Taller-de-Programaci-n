def palindromo(num):
    if isinstance(num, int)and(num>0):
        if (num==palindromo_aux(num, contarDigitos(num)-1)):
            return True
        else:
            return False
    else:
        return "Error, ingrese un número entero positivo."

def contarDigitos(num):
    if num==0:
        return 0
    else:
        return 1+contarDigitos(num//10)

def palindromo_aux(num, contador):
    if num==0:
        return 0
    else:
        return (num%10)*(10**contador)+palindromo_aux(num//10, contador-1)
