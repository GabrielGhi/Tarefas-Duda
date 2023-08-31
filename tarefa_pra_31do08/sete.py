def contar_ocorrencias(lista, elemento):
    contador = 0
    
    for item in lista:
        if item == elemento:
            contador += 1
    
    return contador

elementos = [4, 2, 5, 7, 3, 7, 89, 4, 4, 5, 6]
elemento_alvo = 2
ocorrencias = contar_ocorrencias(elementos, elemento_alvo)
print(f"O elemento {elemento_alvo} aparece {ocorrencias} vezes na lista.")
