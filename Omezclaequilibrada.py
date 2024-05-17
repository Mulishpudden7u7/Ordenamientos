def mezcla_equilibrada(lista):
    if len(lista) <= 1:
        return lista
    
    run_size = 1
    while run_size < len(lista):
        for start in range(0, len(lista), 2 * run_size):
            mid = min(start + run_size, len(lista))
            end = min(start + 2 * run_size, len(lista))
            merged = intercalar(lista[start:mid], lista[mid:end])
            lista[start:start+len(merged)] = merged
        run_size *= 2
    
    return lista

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
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista ordenada:", mezcla_equilibrada(lista))
