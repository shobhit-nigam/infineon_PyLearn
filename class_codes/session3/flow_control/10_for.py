# for

lista = ["aa", "bb", "cc", "yy", "aa", "ee", "ll", "aa", "jj", "cc"]

for i in range(len(lista)):
    if lista[i] == "ee":
        print("ee found at", i)

print(lista.index("ee"))
    
