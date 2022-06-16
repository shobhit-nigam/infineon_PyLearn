listx = ["aa", "bb", "dd", "da", "ta", "at", "hy", "oa"]

listy = []

for val in listx:
    if "a" in val:
        listy.append(val)

print(listy)


listz = [val for val in listx if "a" in val]

print(listz)
