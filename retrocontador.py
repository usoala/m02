def retrocontador(e):
    print("{}".format(e), end="")
    if e > 0:
        print(",", end="")
        retrocontador(e-1)
    else:
        print("")
        
retrocontador(10)

def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0

print(sumatorio(4))