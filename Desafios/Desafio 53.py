frase = str(input('Digite a frase: '))
f1 = frase.split()
f2 = str("".join(f1))
quan=int(len(f2))
rang = int(quan / 2)
for c in range (0, rang):
    if f2[c] != f2[quan-c-1]:
        print('Não é um políndromo')
        exit()
else:
    print('Está frase é um políndromo')


