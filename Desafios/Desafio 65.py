c = 0
q = 1
s=0
n2 = 0
menor = 'a'
maior = 0
while q != 'N':
    c += 1
    n = int(input('Digite um número'))
    n1 = n + 0
    if c == 1:
        menor = n
    s = s + n
    q = str(input('Quer continuar [S/N]?')).upper()
    if n1 >= n2:
        maior = n1
    if n1 <= n2:
        menor = n1
    n2 = n1
print('FIM...')
print(f'A media {s/c}')
print(f'maior = {maior}\nmenor = {menor}')