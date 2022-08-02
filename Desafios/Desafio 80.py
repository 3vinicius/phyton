list = []
c = 0
n = int(input("Adicione o valor: "))
print(f'{n} foi adicionado na posição {0}')
list.append(n)
maior = n
menor = n
while c != 5:
    c += 1
    n = int(input("Adicione o valor: "))
    for z in range(0, len(list)):
        if n > maior:
            p = list.index(maior)
            list.insert(p+1,n)
            maior = n
            print(f'{maior} foi adicionado na posição {p+1}')
            break
        elif n < menor:
            p = list.index(menor)
            list.insert(p,n)
            menor = n
            print(f'{menor} foi adicionado na posição {p}')
            break
        for v in range(0, len(list)):
            if list[v] < n < list[v+1]:
                p = list.index(list[v+1])
                list.insert(p,n)
                print(f'{n} foi adicionado na posição {p}')
                break
print(list)