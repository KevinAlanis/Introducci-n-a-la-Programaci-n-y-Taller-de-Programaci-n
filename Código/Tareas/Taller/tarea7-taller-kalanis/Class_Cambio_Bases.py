class  Cambio_Bases:
    def __init__(self):
        pass

    def cambio_bases_bina_deci(self,num):
        if isinstance(num, int)and(num>=0):
            return self.binario(num, 0),self.decimal(num, 0)
        else:
            return "Error, ingrese un valor válido."

    def binario(self,num, contador):
        if(num==0):
            return 0
        else:
            return (num%2)*(10**contador)+self.binario(num//2, contador+1)

    def decimal(self,num, contador):
        if(num==0):
            return 0
        else:
            return (num%10)*(2**contador)+self.decimal(num//10, contador+1)
