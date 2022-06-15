
fa = open("books.txt", "r")
stra = fa.read(5)

print("read data is -->", stra)
print("cursor is at", fa.tell())

fa.close()
