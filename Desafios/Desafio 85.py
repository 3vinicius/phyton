dados = [[],[]]
for c in range (1, 8):
    p = int(input(f"Digite o {c}° número"))
    if p % 2 == 0:
        dados[0].append(p)
    else:
        dados[1].append(p)
print(dados)
dados[0].sort()
dados[1].sort()
print(dados[0])
print(dados[1])