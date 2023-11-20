#fai un programma (una funzione) che date due liste mi dice se sono anagrammi


def sono_anagrammi(parola1, parola2):
    occorrenze_1={}
    for lettera in parola1: occorrenze_1[lettera] = occorrenze_1.setdefault(lettera, 0) + 1

    occorrenze_2={}
    for lettera in parola2: occorrenze_2[lettera] = occorrenze_2.setdefault(lettera, 0) + 1

    for x,y in zip(parola1,parola2):
        occorrenze_1[x]=occorrenze_1.get(x)+1
        occorrenze_2[y]=occorrenze_2.get(y)+1

    return occorrenze_1 == occorrenze_2

print(sono_anagrammi("ciaco","oaicc"))
