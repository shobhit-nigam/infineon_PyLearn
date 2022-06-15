# global local
ga = 5

def funcx():
    la = 33
    ga = 33
    print("inside the function ga =", ga)
    
print("outside, ga =", ga)
funcx()
print("outside, ga =", ga)
