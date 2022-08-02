from time import sleep
esc = 'CALCULADORA DE NÚMEROS PRIMOS'
print(f'\033[1;31;40m{esc:=^40}\033[m')
print()
n = int(input('Digite um número: '))
for c in range(1 , n):
    if c == 1 or c == n:
        print()
    else:
        if n % c == 0:
            sleep(0.5)
            print(f'O Númro {n} é Composto')
            exit()
else:
    sleep(0.5)
    print(f'O Númro {n} é Primo')
    exit()



