lista = [11, 56, 73, 21, 96, 74, 50, 63, 84]
listb = [56, 78, 30, 25, 61, 29, 43, 81, 100, 33, 76]

listc = list(map(lambda la,lb: la if la>lb else lb , lista, listb))

print(listc)
