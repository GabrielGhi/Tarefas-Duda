def contador_vogais(string):
    vogais = "AEIOUaeiou"
    count = 0
    
    for char in string:
        if char in vogais:
            count += 1
            
    return count


frase = str(input("Digite a sua frase: "))
quantidade_vogais = contador_vogais(frase)
print("A quantidade de vogais na frase é:", quantidade_vogais)
