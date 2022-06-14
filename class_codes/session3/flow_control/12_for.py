# for

lista = ["aa", "bb", "cc", "yy", "aa", "ee", "ll", "aa", "jj", "cc"]

dict_freq = {}
# {"aa":3, "bb":1 , ......}

for i in range(len(lista)):
    if lista[i] not in dict_freq:
        dict_freq[lista[i]] = 1
    else:
        dict_freq[lista[i]] = dict_freq[lista[i]] + 1

print(dict_freq)
    
