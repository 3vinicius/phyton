s = float(input('Qual é o seu salario'))
if s > 1250 :
    v = (s*10/100) + s
    print(f'Seu salrio é de {v}R$')
else:
    v = (s * 15 / 100) + s
    print(f'Seu salrio é de {v}R$')