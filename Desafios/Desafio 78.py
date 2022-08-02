list = [3,2,1,5,7,8,4,5,7]
ord = sorted(list)
print(f'O menor valor: [{list.index(ord[0])}] {ord[0]}')
print()
print(f'O maior valor: [{list.index(ord[len(list)-1])}] {ord[len(list)-1]}')
