def quadrado(base, altura):
    for _ in range(altura):
        linha = "* " * base
        print(linha)

# Exemplo de uso
base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))
quadrado(base, altura)
