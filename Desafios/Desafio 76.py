list = ('Lapiz', 1.75, 'Borracha','2.00','Caderno',15.90,"Estojo",25.00,"Transferidor",4.20,'Compasso',9.99,'Mochila',120.32,"Cadernetas",22.30,'Livro',34.90)
print('_'*45)
print(' {:^45}'.format('LISTAGEM DE PREÇOS'))
print('_'*45)
for c in range(0, len(list)):
    if c%2 == 0:
        a = 30 - (len(list[c]))
        print(f'{list[c]}','.'*a, end='')
    else:
        p = str(list[c])
        print(f' R$ {list[c]:>7}')
print('_'*45)
