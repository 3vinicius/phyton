nome = input('Olá, diga seu nome completo ')
print(f'nome maiúsculo é: {nome.upper()}')
print(f'nome minúsculo é: {nome.lower()}')
frase = nome.split()
frasej = ''.join(frase)
print(f'Quantidades de letras que tem é {len(frasej)}')
print(f'Seu primeiro nome tem {len(frase[0])} letras')

