class SumarNumeros:
    def __init__(self):
        pass

    def sumar(self,numero):
        suma = numero
        while(numero != 0):
            numero = int(input("Digite un numero distinto de cero para sumar, o igual a cero para finalizar: "))
            suma = suma+numero
            
        return suma
                

    

    
