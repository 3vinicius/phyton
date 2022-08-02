import requests

try:
    response = requests.get('http://www.pudim.com.br/')
except:
    print("Não é possível acessar o site")
else:
    print('É possivel acessar o site')
