def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    izquierda = mezcla_directa(lista[:mitad])
    derecha = mezcla_directa(lista[mitad:])
    
    return intercalar(izquierda, derecha)

def intercalar(lista1, lista2):
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
lista = [5, 3, 8, 4, 2, 7, 1, 6]
print("Lista ordenada:", mezcla_directa(lista))
