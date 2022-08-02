from time import sleep
n1 = float(input('Digite a nota da AB1: '))
n2 = float(input('Digite a nota da AB2: '))
m = (n1 + n2)/2
sleep(0.5)
if m < 5:
    print('Média abaixo de 5.0 \n\033[1;31mREPROVADO\033[m')
elif 5 < m < 6.9 :
    print('Média entre 5.0 e 6.9\n\033[1;32mRECUPERAÇÃO\033[m')
else:
    print('Média 7 ou superior\n\033[1;34mAPROVADO\033[m')