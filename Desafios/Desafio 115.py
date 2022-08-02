# Imports
from uteis import dado

# Funções
def menu():
    print('-'*40)
    print(F'{"MENU PRINCIPAL":^40}')
    print('-'*40)
    print('1 - Verdados cadastrados')
    print('2 - Cadastrar pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)
    global op
    op = dado.leiaint(input('Digite uma das opções: '))
def vercadastro():
    print('-' * 40)
    try:
        a = open('lista', 'rt')
    except:
        print('Ocorreu um erro')
    else:
        for linha in a:
            escreva = linha.split(';')
            escreva[1] = escreva[1].replace('\n','')
            print(f'{escreva[0]:<20}{escreva[1]:>3}')
def novocadastro():
    print('-' * 40)
    print(F'{"NOVO CADASTRO":^40}')
    print('-' * 40)
    nome = dado.leianome(input('Digite seu nome'))
    nome = str(nome)
    idade = dado.leiaint(input('Digite sua idade'))
    idade = str(idade)
    print('-' * 40)
    ecrevatxt('lista', nome, idade)
def ecrevatxt(aq, nome, idade):
    try:
        a = open(aq, 'at')
    except:
        print('Ocorreu um erro')
    else:
        a.write(f'{nome};{idade}\n')
        a.close()
def arquivoex():
    try:
        a = open('lista', 'rt')
        a.close()
    except:
        a = open('lista', 'wt+')
        a.close()
    else:
        pass



# Variaveis
op = 0

listadedados = []

arquivoex()

#Progama principal
while True:
    menu()
    if op == 1:
        vercadastro()
    if op == 2:
        novocadastro()
    if op == 3:
        print("Finalizando progama")
        break

