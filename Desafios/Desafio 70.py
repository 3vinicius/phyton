a = "S"
s = 0
n2 = 99999999999999999
caro = 0
while a != 'N':
    print('=' * 10, 'NOVO CADASTRO', '=' * 10)
    nome = str(input("Nome do Produto: "))
    preco = float(input('Preço do Produto: '))
    s = s + preco
    if preco > 1000:
        caro += 1
    new = preco
    if new < n2:
        barato = new
        n2 = new
        nomebarato = nome
    a = str(input('Deseja realizar um novo cadastro? [S/N]')).upper()
print('Fim do Progama')
print('='*10, 'DADOS', '='*10)
print(f'TOTAL: {s}')
print(f'{caro} produtos custaram mais de 1000$ ')
print(f'{nomebarato} foi o produto mais barato e custou {barato}$')
