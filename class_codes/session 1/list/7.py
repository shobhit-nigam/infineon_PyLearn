
avengers = ["thor", "ironman", "black widow", "captain"]

marvel = ["magneto", "moon knight", avengers]

print("marvel = ", marvel);
print("----")
marvel[0][0] = 'T'
#error
print("marvel = ", marvel);
