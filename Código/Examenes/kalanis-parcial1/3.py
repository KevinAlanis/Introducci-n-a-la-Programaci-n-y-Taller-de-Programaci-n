def contarConsonantes(texto):
    if isinstance(texto, str):
        return contarConsonantes_aux(texto)
    else:
        return "Error, ingrese una cadena de texto"

def contarConsonantes_aux(texto):
    if (texto==''):
        return 0
    if (texto[0]!='a')and(texto[0]!='e')and(texto[0]!='i')and(texto[0]!='o')and(texto[0]!='u'):
        return 1+contarConsonantes_aux(texto[1:])
    else:
        return contarConsonantes_aux(texto[1:])
