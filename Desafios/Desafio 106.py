def manual(a):
    if a == "Fim":
        ''
    help(a)
print('\033[1;32;43m-\033[m'*20)
print(f'{"AJUDA HELP":^20}')
print('-'*20)
manual(input('Digite o que quer pesquisar'))