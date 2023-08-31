def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

# Exemplo de uso
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado_potencia = calcular_potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a:", resultado_potencia)