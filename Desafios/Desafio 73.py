list = ('América-MG','Athletico','Atlético-GO','Atlético-MG','Avaí','Botafogo' ,'Bragantino','Ceará','Chapecoence','Corinthians','Coritiba','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Juventude','Internacional','Palmeiras Santos' ,'São Paulo')
#for c in range(0, len(list)):
   #print(f'[{c+1}]'' 'f'{list[c]}')
print("5 Primeiros colocados do Brasileirão")
for a in range(0, 4):
    print(f'[{a+1}]'' 'f'{list[a]}')
print("-"*20)
print("4 Ultimos colocados do Brasileirão")
for b in range(len(list)-1,15,-1):
    print(f'[{b+1}]'' 'f'{list[b]}')
print("-"*20)
a = sorted(list)
print("Times em ordem Alfabetica")
for c in range(0, len(list)):
   print(f'[{c+1}]'' 'f'{a[c]}')
print("-" * 20)
p = list.index('Chapecoence')
print(f'[{p+1}] Chapecoence')
