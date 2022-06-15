
with open("books.txt", "r") as fa:
    stra = fa.read()

print("read data is -->", stra)
#print("read data is -->", strb)

lista = stra.split()
print(lista)
