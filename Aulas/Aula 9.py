n1 = float(input('Digite a priemira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2)/2
print(f'A sua média é {m:.1f}')
if m >= 6:
    print('Parabéns voçê passou')
else:
    print('Infelizmente voçê não passou, mas não se preocupe. Ainda há esperança !')