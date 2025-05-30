def histogram(texto):
    histograma ={}
    for letra in texto:
        if letra in histograma:
            histograma[letra] +=1
        else:
            histograma[letra]= 1

    for letra in histograma:
        print(letra + ":" + "*" * histograma[letra])        
    
histogram("inconstitucionalissimamente")