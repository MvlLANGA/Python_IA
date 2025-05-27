#def anagrams():
#    texto = input("Primeria palavra: ")
#    palavra = input("Segunda palavra: ")
#    return sorted(texto) == sorted(palavra)
#print(anagrams())
    

# ou da pra fazer assim

def anagrams(texto, palavra):
    return sorted(texto) == sorted(palavra)

print(anagrams("amar", "rama"))
print(anagrams("tabby", "batty"))