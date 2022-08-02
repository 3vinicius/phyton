def numeroint(n):
    while True:
        if n.isnumeric():
            return n
        print('\033[31mERRO:\033[m')
        n = input('Digite um valor númerico')

v = numeroint(input("Digite o número"))
print(f'O número {v} é um núemro inteiro')