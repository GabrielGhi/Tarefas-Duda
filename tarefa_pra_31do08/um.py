def maior_numero(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]  # Começamos assumindo que o primeiro número é o maior
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [12, 45, 6, 78, 23, 9, 67]
resultado = maior_numero(numeros)
print(f"O maior número na lista é: {resultado}")
