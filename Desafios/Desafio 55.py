p1 = int(input('Peso da pesosa 1'))
p2 = int(input('Peso da pesosa 2'))
p3 = int(input('Peso da pesosa 3'))
p4 = int(input('Peso da pesosa 4'))
p5 = int(input('Peso da pesosa 5'))
p6 = int(input('Peso da pesosa 6'))
p7 = int(input('Peso da pesosa 7'))
list1 = [p1, p2, p3, p4, p5, p6, p7]
for d in range(0, 7):
    if list1[d] >= list1[0] and list1[d] >=list1[1] and list1[d] >=list1[2] and list1[d] >=list1[3] and list1[d] >=list1[4] and list1[d] >=list1[5] and list1[d] >=list1[6]:
        print(f'{list1[d]} é o maior peso')
    elif list1[d] <= list1[0] and list1[d] <= list1[1] and list1[d] <= list1[2] and list1[d] <= list1[3] and list1[d] <= list1[4] and list1[d] <= list1[5] and list1[d] <= list1[6]:
        print(f'{list1[d]} é o menor peso')


