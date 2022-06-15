
fa = open("books.txt", "r")
stra = fa.read(5)

print("read data is -->", stra)
print("cursor is at", fa.tell())

fa.seek(9)
# jump 9 bytes from the start
stra = fa.read(6)
print("read data is -->", stra)
print("cursor is at", fa.tell())

fa.close()
