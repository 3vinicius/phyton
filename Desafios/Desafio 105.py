def notas (*a, sit=False):
    bibli = {}
    maior = 0
    menor = 999999
    bibli['Quat. de Notas'] = a[0]
    for p in range(0, len(a)):
        if a[p] >= maior:
            maior = a[p]
        if a[p] <= menor:
            menor = a[p]
    bibli['Maior Nota'] = maior
    bibli['Menor Nota'] = menor
    bibli['Média das notas'] = (sum(a) - a[0]) / a[0]
    if sit == True:
        if bibli['Média das notas'] < 6:
            bibli['Situação'] = 'Ruim'
        if 6 <= bibli['Média das notas'] < 8:
            bibli['Situação'] = 'Bom'
        if bibli['Média das notas'] >= 8:
            bibli['Situação'] = 'Excelente !'
    return bibli




l = notas(3, 7, 3, 9, sit=True)
print(l)
