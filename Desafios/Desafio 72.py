list = ('Zero', "Um", "Dois", "Três", "Quatro", 'Cinco', 'Seis', 'Sete', 'Oito', "Nove", "Dez", "Onze", "Doze", "Treze", "Quartoz", "Quinze", "Dezeseis", "Desezete", "Dezoito", "Dezenova", "Vinte")
a = int(input("Digite o número"))
while True:
    if 0 <= a <= 20:
        print(list[a])
        break
    else:
        a = int(input("Digite o número entre 0 e 20"))