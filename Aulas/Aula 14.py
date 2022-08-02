c = 1
p = 0
i = 0
while c != 0:
    c = int(input("Digite um valor"))
    if c % 2 == 0 and c != 0:
        p += 1
    if c % 2 != 0:
        i += 1
print(f'{p} par \n{i} impar')
print('Fim')

