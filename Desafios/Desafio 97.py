# Função escrever:

def escrever(*a):
    print('-'*len(a[0]))
    print(f'{a[0]:^{len(a[0])}}')
    print('-' * len(a[0]))
text = str(input("Digite o texto: "))
escrever(text)
