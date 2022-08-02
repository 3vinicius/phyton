list = [[],[],[]]
for c in range(0, 3):
    r = int(input(f"Digite o valor [{0},{c}] "))
    list[0].append(r)
for d in range(0, 3):
    e = int(input(f"Digite o valor [{1},{d}] "))
    list[1].append(e)
for q in range(0, 3):
    f = int(input(f"Digite o valor [{2},{q}] "))
    list[2].append(f)
print(f'  [  {list[0][0]}  ]',f'[  {list[0][1]}  ]',f'[  {list[0][2]}  ] \n'
     ,f' [  {list[1][0]}  ]',f'[  {list[1][1]}  ]',f'[  {list[1][2]}  ] \n'
     ,f' [  {list[2][0]}  ]',f'[  {list[2][1]}  ]',f'[  {list[2][2]}  ] ')




