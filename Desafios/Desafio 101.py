import datetime
def votacao(ano):
    a = datetime.date.today().year - ano
    print(f'Com {a} anos o voto', end=' ')
    if a < 18:
        print(f'NÃO É OBRIGATORIO')
    if a >= 18 and a < 65:
        print(f'VOTO OBRIGATORIO')
    if a >= 65:
        print(f'VOTO É OPCIONAL')

votacao(int(input("Qual o seu ano de nascimento ?")))
