def calcular_media(lista):
    if not lista:
        return None
    
    total = sum(lista)
    media = total / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media_numeros = calcular_media(numeros)
print("A média dos números é:", media_numeros)
