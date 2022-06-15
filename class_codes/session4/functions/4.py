lista = [11, 56, 73, 21, 96, 74, 50, 63, 84]
listb = [56, 78, 30, 25, 61, 29, 43, 81, 100, 33, 76]

def funca(la, lb):
    lc = la + lb*2 + 10
    return lc

listd = list(map(funca, lista, listb))
print(listd)

def funca(la):
    return la**2

print(list(map(funca, lista)))
