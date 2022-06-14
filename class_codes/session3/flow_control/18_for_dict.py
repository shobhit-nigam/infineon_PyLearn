# for with sequence

avengers = {"ironman":"suit", "captain":"shield", "hawkeye":"arrow", "thor":"hammer"}

for x in avengers:
    print("x =", x)

print("----")

for x in avengers.values():
    print("x =", x)

print("----")

for k, v in avengers.items():
    print("k =", k, "v =", v)
