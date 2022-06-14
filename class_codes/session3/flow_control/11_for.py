# for

lista = ["aa", "bb", "cc", "yy", "aa", "ee", "ll", "aa", "jj", "cc"]

list_index = []

for i in range(len(lista)):
    if lista[i] == "aa":
        list_index.append(i)

print(list_index)

    
