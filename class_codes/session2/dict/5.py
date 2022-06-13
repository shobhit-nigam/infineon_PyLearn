avengers = {"ironman":"suit", "captain":"shield", "hawkeye":"arrow", "thor":"hammer"}


dc = ["batman", "wonder woman", "flash"]

heroes = {"dc_key":dc, "ave":avengers}


print(heroes)
print("-----")
print(heroes["ave"])
print("-----")
print(heroes["ave"]["ironman"])
print("-----")
print(heroes["ave"]["ironman"][2])
