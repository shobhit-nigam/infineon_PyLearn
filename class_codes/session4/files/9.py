with open("books.txt", "r") as fa:
    lista = fa.readlines()
    
with open("the_books.txt", "w") as fb:
    for line in lista:
        if "the" in line.lower():
            fb.write(line)
