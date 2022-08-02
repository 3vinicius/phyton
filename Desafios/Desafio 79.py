d = 'S'
list = []
while d != 'N':
    v = int(input("Qual valor você quer adicionar ?"))
    if v in list:
        print('Esse valor já existe na lista')
    else:
        list.append(v)
    d = input("Voçê deseja adicionar mais valores [S/N]").upper()
for n in sorted(list):
    print(n)