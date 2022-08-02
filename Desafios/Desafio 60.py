n = int(input('Digite um número'))
c = n + 0
f = 1
while c != 1:
    c -= 1
    f = f*n*c
    n = 1
print(f)