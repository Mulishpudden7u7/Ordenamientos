def intercalacion(lista1, lista2):
    resultado = []
    i, j = 0, 0
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
            
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    
    return resultado

# Ejemplo de uso
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
print("Lista ordenada:", intercalacion(lista1, lista2))
