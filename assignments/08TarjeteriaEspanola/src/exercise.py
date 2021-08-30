def tarjetas(pliegos,plumones):
    t=pliegos*12
    p=plumones*35
    if t<=p:
        return t
    elif p<=t:
        return p
def main():
    #escribe tu código abajo de esta línea
    pliegos=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    print("El número máximo de tarjetas que se pueden hacer es:",tarjetas(pliegos,plumones))
pass
