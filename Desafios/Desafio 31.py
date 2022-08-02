d = float(input('Qual a distancia da viagem em Km ? '))
if d <= 200:
    v = d*0.5
else:
    v = d*0.45
print(f'O valor a ser pago é de {v}')