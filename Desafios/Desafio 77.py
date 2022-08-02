list1 = ('aprender', 'programar', 'linguagem', 'phyton',
        'curso', 'gratis','estudar', 'praticar',
        'trabalhar', 'mercado', 'programador','futuro')
b = 0
while b != 1:
    for c in range(0, len(list1)):
        print(f'Na palavra {str(list1[c]).upper()} temos as vogais: ',end='')
        a = list1[c].count('a')
        print('a '*a,end='')
        e = list1[c].count('e')
        print('e ' * e,end='')
        i = list1[c].count('i')
        print('i ' * i,end='')
        o = list1[c].count('o')
        print('o ' * o,end='')
        u = list1[c].count('u')
        print('u '*u)
    b += 1







