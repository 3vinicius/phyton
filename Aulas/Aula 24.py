while True:
    try:
        a = int(input('Digite um númerto'))
    except Exception as erro:
        print(f'Infelizmente tivemos um problema{erro.__class__}')
    else:
        b = 5 / a
        print(f'O resultado é {b:.1f} ')
        break

