with open("books.txt", "r") as fa:
    lista = fa.readlines()
    

for line in lista:
    if "the" in line.lower():
        print(line)
