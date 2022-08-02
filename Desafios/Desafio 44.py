valor = float(input('Preço do produto'))
condicao = str(input('condição de pagamnteo'))
print()
if condicao == 'dinheiro' or condicao == 'cheque':
    vp = valor - ((10/100)*valor)

elif condicao == "a vista no cartão":
    vp = valor - ((5 / 100) * valor)

elif condicao == "2x no cartão":
    vp = valor

else:
    vp = valor + ((20 / 100) * valor)
print(vp)