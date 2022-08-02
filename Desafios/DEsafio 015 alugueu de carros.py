d = int(input('Por quantos dias o carro foi alugado? : '))
km = float(input('Quantos Km o carro percorreu? : '))
p = (60 * d) + (0.15 * km)
print(f'Total a pagar: {p:.2f}')
