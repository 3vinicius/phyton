n1 = float(input("digite o primeto número"))
n2 = float(input("digite o segundo número"))
n3 = float(input("digite o terceiro número"))
if n1 > n2:
    if n1 > n3:
        print(f'{n1} é o maior número')
else:
    print()
if n2 > n3:
    if n2 > n1:
        print(f'{n2} é o maior número')
else:
    print()
if n3 > n1:
    if n3 > n2:
        print(f'{n3} é o maior número')
else:
    print()
if n1 < n2:
    if n1 < n3:
        print(f'{n1} é o menor número')
else:
    print()
if n2 < n1:
    if n2 < n3:
        print(f'{n2} é o menor número')
else:
    print()
if n3 < n1:
    if n3 < n2:
        print(f'{n3} é o menor número')
else:
    print()