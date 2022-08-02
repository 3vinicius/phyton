e = str(input("Digite a expressão"))
list = []
len(e)
for c in range(0, len(e)):
    list.append(e[c])
q = list.count(')')
w = list.count('(')
if q%2 == 0 and w%2 ==0 :
    print('A espressão está correta')
else:
    print('A expressão está errada')

