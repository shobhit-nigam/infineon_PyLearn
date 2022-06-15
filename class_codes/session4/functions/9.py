lista = [11, 56, 73, 21, 96, 74, 50, 63, 84]
listb = [56, 78, 30, 25, 61, 29, 43, 81, 100, 33, 76]

listc = list(filter(lambda lb: lb%2==0 and lb%5==0, listb))

print(listc)
