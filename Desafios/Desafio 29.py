vel = float(input('Qual a velocidade do carro em km/h '))
e = float(vel - 80)
m = e * 7
if vel <= 80:
    print('Parabéns, você está dentro do limite. \nDireção segura salva vidas')
else:
    print(f'Voçe foi multado em {m}R$ por exceter {e}km/h')