valor = float(input('Quanto Voçê ganha hora?'))
hora = float(input('Quantas horas voçê trabalha por semana ?'))
SALB = valor*hora*5
IR =  SALB*(11 / 100)
INSS = SALB *(8 / 100)
SIND = SALB *(5 / 100)
SALAL = SALB - INSS - INSS
print(f'+ Saalário Bruto: {SALB:.2f} R$\n- IR (11%): {IR:.2f} R$\n- Sindicato (5%): {SIND:.2f} R$\n = Salário Liquido: {SALAL:.2f}R$')
