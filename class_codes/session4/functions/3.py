lista = [11, 56, 73, 21, 96, 74, 50, 63, 84]
listb = [56, 78, 30, 25, 61, 29, 43, 81, 100, 33, 76]

def funca(la, lb):
    lc = la + lb*2 + 10
    return lc

listc = []

if len(lista) <= len(listb):
    for i in range(len(lista)):
        listc.append(funca(lista[i], listb[i]))
else:
    for i in range(len(listb)):
        listc.append(funca(lista[i], listb[i]))

print(listc)


listd = list(map(funca, lista, listb))
print(listd)
