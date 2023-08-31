def verificar_anagrama(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    if len(str1) != len(str2):
        return False
    
    
    count_dict1 = {}
    count_dict2 = {}
    
    
    for char in str1:
        count_dict1[char] = count_dict1.get(char, 0) + 1
    for char in str2:
        count_dict2[char] = count_dict2.get(char, 0) + 1
    
    
    return count_dict1 == count_dict2


palavra1 = str(input("Digite a 1 palavra: "))
palavra2 = str(input("Digite a 2 palavra: "))
print(verificar_anagrama(palavra1, palavra2))
