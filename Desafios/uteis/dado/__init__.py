def leiadinheiro(a):
    """if "," in a:
       a = a.replace(',','.').strip"""
    while True:
        try:
            if ',' in a:
                a = a.replace(',','.')
            v = float(a)
        except:
            print('\033[31mErro: Valor invalido\033[m')
            a = input('Digite o valor: ')
        else:
            if "." in a:
                a = a.replace('.', ',')
            return a

def leiaint(msg):
    while True:
        try:
            if ',' in msg:
                msg = msg.replace(',','.')
            v = int(msg)
        except:
            print('\033[31mErro: valor invalido\033[m')
            msg = input('Digite um número inteiro')
        else:
            return int(v)

def leiafloot(msg):
    while True:
        try:
            if ',' in msg:
                msg = msg.replace(',', '.')
            v = float(msg)
        except:
            print('\033[31mErro: Valor invalido\033[m')
            msg = input('Digite um número real')
        else:
            return float(v)

def leianome(msg):
    while True:
        try:
             msg.isalpha() == True
        except:
            print('\033[31mErro: Digite um nome valido\033[m')
            msg = input('Digite um nome')
        else:
            return msg

