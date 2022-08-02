peso = float(input("Digite o peso"))
alt = float(input('Digite a altura'))
IMC = peso/(alt**2)
print(f"Meu IMC = {IMC:.2f}")
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif IMC <= 40:
    print('Obesidade Mórbita')


