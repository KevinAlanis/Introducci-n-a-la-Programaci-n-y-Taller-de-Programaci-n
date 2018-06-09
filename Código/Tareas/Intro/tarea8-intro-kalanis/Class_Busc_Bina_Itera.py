class BusquedaBinaria:
    def __init__(self):
        pass

    def busc(self,x,lista):
        if isinstance(lista, list)and(lista!=[]):
            return self.buscar(lista,x,False)
        else:
            "Error"

    def buscar(self,lista,x,encontrado):
        for i in range(len(lista)):
            if x==lista[(len(lista)-1)//2]:
                encontrado=True
            if x<lista[(len(lista)-1)//2]:
                lista=lista[:(len(lista)-1)//2]
            else:
                lista=lista[(len(lista)-1)//2:]
        return encontrado
                

    

    
