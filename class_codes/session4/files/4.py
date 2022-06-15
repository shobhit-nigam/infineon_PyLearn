
with open("books.txt", "r") as fa:
    stra = fa.readline()
    strb = fa.read(5)

print("read data is -->", stra)
print("read data is -->", strb)

print(fa.closed)
