import moeda
print(f'{"Seja bem vindo ao conversor de moedas":=^50}')
print()

v = float(input('Qual o valor deseja calcular ?'))
print(f'O valor digitado foi {moeda.valormone(v)}')
print(f'A metade de {moeda.valormone(v)} é {moeda.valormone(moeda.metade(v))}')
print(f'O dobro de {moeda.valormone(v)} é {moeda.valormone(moeda.dobro(v))}')
print(f'10% de aumento de {moeda.valormone(v)} é {moeda.valormone(moeda.aumentado10(v))}')
print(f'13% de redução de {moeda.valormone(v)} é {moeda.valormone(moeda.reduz13(v))}')
