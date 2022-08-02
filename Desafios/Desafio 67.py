text1 = 'TABUADA'
print(f'\033[m{text1:^20}')
print()
while True:
    n = int(input('Digite o número da tabuada'))
    if n < 0:
        break
    for c in range(0, 11):
        b = c + 0
        print(f'{n} X {b}')
    print('-'*20)
print('FIM....')