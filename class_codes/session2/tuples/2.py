avengers = ["thor", "ironman", "black widow", "captain"]
print("avengers =", avengers)
print("type of avengers =", type(avengers))
print("------")
      
avengers = ("thor", "ironman", "black widow", ["captain america", "captain marvel"] )
print("avengers =", avengers)
print("type of avengers =", type(avengers))

avengers[-1][0] = "CAPTAIN america"

print("------")
      
print("avengers =", avengers)
#error
#avengers[0] = "Thor"





