def factor(f, show):
    """factor(f = número, show = True  )
    ==> f : número que deseja calcular
    show: parametro que define se quer mostrar
    ou não a multiplicação do fatorial.
    show = True --> Mostrar a multiplicação
    show = False --> Não mostrar a multiplicação
    """
    t = 1
    for n in range(f, 0, -1):
        if show == True:
            print(f'{n} x', end=' ')
        t = t * n
    print(f'= {t}')



factor(5, show=True)
help(factor)