# define a function
# variable number of arguments
# args 

def greet(la, lb, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("-----_")
    for val in args:
        print(val)

