def encontrar_substring(string, substring):
    return substring in string

texto = str(input("Digite a frase: "))
sub = str(input("Digite a palavra: "))
resultado = encontrar_substring(texto, sub)
print(resultado)  
