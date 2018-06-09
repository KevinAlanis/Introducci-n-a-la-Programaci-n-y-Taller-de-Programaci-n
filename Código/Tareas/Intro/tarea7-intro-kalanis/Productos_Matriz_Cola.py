def multiplicar_matriz(matriz1,matriz2):
    if isinstance(matriz1, list)and(matriz1!=[])and(matriz2, list)and(matriz2!=[])and (len(matriz1)==len(matriz2[0])):
        return multiplicar(matriz1,matriz2,len(matriz1),len(matriz1[0]),0,0,len(matriz2),len(matriz2[0]),0,0,0,0,formarMatriz(matriz1,0,[]),0)
    else:
        return "Error"

def formarMatriz(matriz1,contador,matriz3):
    if contador==len(matriz1):
        return matriz3
    else:
        return formarMatriz(matriz1,contador+1,matriz3+[[]])

def multiplicar(matriz1,matriz2,num_f1,num_c1,f1,c1,num_f2,num_c2,multi,suma,f2,c2,matriz3,indic):
    if (f1==num_f1):
        return matriz3
    if ((c1==num_c1) and ((c2+1)==num_c2)):
        return multiplicar(matriz1,matriz2,num_f1,num_c1,f1+1,0,num_f2,num_c2,multi,0,0,0,matriz3,indic+1)
    if (f2==num_f2):
        return multiplicar(matriz1,matriz2,num_f1,num_c1,f1,0,num_f2,num_c2,multi,0,0,c2+1,[matriz3[indic]]+[[suma]],0)
    else:
        return multiplicar(matriz1,matriz2,num_f1,num_c1,f1,c1+1,num_f2,num_c2,matriz1[f1][c1]*matriz2[f2][c2],suma+multi,f2+1,c2,matriz3,0)
