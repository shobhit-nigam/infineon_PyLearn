
fa = open("books.txt", "r")
stra = fa.read(5)
print("type of stra =",type(stra))
print("read data is -->", stra)
fa.close()
