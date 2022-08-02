import time
print('='*10,'\033[1;31mEMPRESTIMO BANCARIO\033[m','='*10)
print()
vc = float(input('Qual o valor da casa ? '))
s = float(input('Qual o seu salario ? '))
t = float(input('Quantos anos voçê quer pagar ? '))
time.sleep(1)
pm = vc / (t*12)
if pm<= s*(30/100) :
    print("\033[1;34mEMPRESTIMO CONCEDIDO \033[m")
    print(f'O valor da prestção é de {pm:.2f}R$')
else:
    print('\033[1;31mEmprestimo negado!')