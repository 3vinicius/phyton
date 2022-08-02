def ficha(nome = '<desconhecido>', gols = '0'):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0:
        gols = 0
    print(f'O jogador {nome}, fez {gols} gols. ')


ficha(input("Qual o nome do jogador"), input("Quantos gols ele marcou ?"))