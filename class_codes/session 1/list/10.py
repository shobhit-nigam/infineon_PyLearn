
avengers = ["thor", "ironman", "black widow", "captain"]

marvel = ["magneto", "moon knight", "spiderman"]

print("avengers =", avengers)
print("marvel =", marvel)
marvel.append(avengers)
print("marvel =", marvel)
print("------")
avengers = ["thor", "ironman", "black widow", "captain"]

marvel = ["magneto", "moon knight", "spiderman"]

marvel.extend(avengers)
print("marvel =", marvel)
