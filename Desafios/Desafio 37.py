numero = int(input('Digite um número inteiro'))
print()
b = int(input('''1 - Binário
2 - Octal
3 - Hexadecimal
\033[1mEscola uma das bases: \033[m\n''' ))
if b == 1:
     b = bin(numero)
     print(b[2::])
elif b == 2:
    o = oct(numero)
    print(o[2::])
elif b == 3:
    h = hex(numero)
    print(h[2::])
else:
    print('\033[1;31mERRO')