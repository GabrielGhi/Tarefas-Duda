def calcular_desconto(valor_produto, percentual_desconto):
    desconto = valor_produto * (percentual_desconto / 100)
    valor_com_desconto = valor_produto - desconto
    return valor_com_desconto

valor_original = int(input("Digite o valor: "))
percentual_desconto = int(input("Digite o valor do desconto: "))
valor_com_desconto = calcular_desconto(valor_original, percentual_desconto)
print(f"O valor com desconto é: R${valor_com_desconto:.2f}")
