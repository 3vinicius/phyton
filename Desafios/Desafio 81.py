import random
list = []
for c in range(0, random.randint(0,100)):
    num = list.append(random.randint(0,99))
len(list)
print(f'{len(list)} números foram digitados')
list.sort(reverse=True)
print(list)
if 5 in list:
    print('O número 5 está na lista')
else:
    print('O numero 5 não está na lista')