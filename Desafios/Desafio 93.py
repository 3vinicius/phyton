bibl = {}
bibl['nome'] = str(input("Digite o nome do jogador"))
p = int(input('Quantas partidas'))
s = 0
gols = []
for c in range(0,p):
    golsv = int(input(f'Quantos gols marcou na {c+1}° partida'))
    gols.append(golsv)
    s += golsv
print('=-'*20)
bibl['gols'] = gols
bibl['total'] = s
print(bibl)
print('=-'*20)
for k,v in bibl.items():
    print(f'{k}: {v}')
print('=-'*20)
print(f'O jogador {bibl["nome"]} jogou {p} partidas')
for i, v in enumerate(gols):
    print(f'=> Na {i+1}° partida ele marcou {v} gols')
print(f'Um total de {bibl["total"]} gols')
