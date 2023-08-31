def quadrado(base, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            linha = "* " * base
        else:
            linha = "* " + "  " * (base - 2) + "*"
        print(linha)

base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))
quadrado(base, altura)
