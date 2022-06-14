# for with sequence

lista = ["aa", "bb", "cc", "yy", "aa", "ee", "ll", "aa", "jj", "cc"]

dict_freq = {}

for x in lista:
    if x not in dict_freq:
        dict_freq[x] = 1
    else:
        dict_freq[x] = dict_freq[x] + 1

print(dict_freq)
