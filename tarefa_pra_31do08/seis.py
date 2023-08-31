def encontrar_primos(numero):
    primos = []
    
    for num in range(2, numero + 1):
        if e_primo(num):
            primos.append(num)
    
    return primos

def e_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 17625346
numeros_primos = encontrar_primos(n)
print("Números primos menores ou iguais a", n, "são:", numeros_primos)
