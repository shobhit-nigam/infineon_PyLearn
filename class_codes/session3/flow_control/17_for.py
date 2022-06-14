# for with sequence

lista = ["aa", "bb", "cc", "yy", "aa", "ee", "ll", "aa", "jj", "cc"]

for x in lista:
    if x == "ee":
        print("found it")
        break
else:
    print("didn't find it")


print("-----")


for x in lista:
    if x == "zz":
        print("found it")
        break
else:
    print("didn't find it")
