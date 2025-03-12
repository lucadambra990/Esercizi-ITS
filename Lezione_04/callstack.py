def alpha():
    print("Executing alpha")

def beta():
    alpha()
    print("Executing beta")

def gamma():
    print("Executing gamma")
    beta()

gamma()