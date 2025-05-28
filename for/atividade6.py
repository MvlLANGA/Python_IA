def sem_vogal(texto):
    vogais = "aeiou"
    nova_string = ""

    for letra in texto:
        if letra not in vogais:
            nova_string += letra
    return nova_string
print(sem_vogal("samambaia"))
