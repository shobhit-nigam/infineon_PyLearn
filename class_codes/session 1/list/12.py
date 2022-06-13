
avengers = ["thor", "ironman", "black widow", "captain"]

marvel = ["magneto", "moon knight", "spiderman", avengers.copy()]
#reference 
x = avengers.copy()

print("avengers =", avengers)
print("marvel =", marvel)
print("x =", x)

avengers.append("wanda")
avengers.sort()
avengers.pop()
print("avengers =", avengers)
print("marvel =", marvel)
print("x =", x)
