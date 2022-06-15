
with open("books.txt", "r") as fa:
    stra = fa.read()

print("read data is -->", stra)

# string function
lista = stra.splitlines()
print(lista)
