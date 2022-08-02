frasen = input('Digite uma frase: ')
frase = frasen.upper()

frase1 = frase.split()
frase2 = ''.join(frase1)


print(f'Quantas vezes aparece a letra A {frase.count("A")}')
print(f'A que posição aparece o A pela primeira vez {frase.find("A")} ')
print(f'A letra A aparece a ultima vez na posição {frase.rfind("A")}')
