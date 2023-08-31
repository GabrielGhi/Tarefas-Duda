def calcular_raiz_quadrada(numero):
    aprx = numero ** 0.5  # Aproximação inicial
    return round(aprx, 2)

numero = int(input("Digite o numero: "))
raiz_quadrada = calcular_raiz_quadrada(numero)
print("A raiz quadrada de", numero, "é aproximadamente:", raiz_quadrada)