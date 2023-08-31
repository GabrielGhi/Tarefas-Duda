def verificar_palindromo(string):
    string = string.replace(" ", "").lower()
    
    return string == string[::-1]

palavra = str(input("Digite a frase: "))
print(verificar_palindromo(palavra))