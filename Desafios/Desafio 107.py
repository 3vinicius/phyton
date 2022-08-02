import moeda
print(f'{"Seja bem vindo ao conversor de moedas":=^50}')
print()

v = float(input('Qual o valor deseja calcular ?'))
print(f'O valor digitado foi {v}')
print(f'A metade de {v} é {moeda.metade(v)}')
print(f'O dobro de {v} é {moeda.dobro(v)}')
print(f'10% de aumento de {v} é {(moeda.aumentado10(v))}')
print(f'13% de redução de {v} é {moeda.reduz13(v)}')
