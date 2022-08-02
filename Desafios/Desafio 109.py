import moeda
print(f'{"Seja bem vindo ao conversor de moedas":=^50}')
print()

v = float(input('Qual o valor deseja calcular ?'))
print(f'O valor digitado foi {moeda.valormone(v)}')
print(f'A metade de {v} é {moeda.metade(v, format=True)}')
print(f'O dobro de {v} é {moeda.dobro(v,format=True)}')
print(f'10% de aumento de {v} é {(moeda.aumentado10(v, 10, format=True))}')
print(f'13% de redução de {v} é {moeda.reduz13(v, 13, format=True)}')
