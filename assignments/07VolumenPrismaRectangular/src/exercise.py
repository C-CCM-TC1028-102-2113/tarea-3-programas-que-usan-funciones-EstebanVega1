def arearect(base,altura):
    global area
    area=base*altura
    return area
def volumen(area,profundidad):
    vol=area*profundidad
    return vol
def main():
    base=float(input("Dame la base: "))
    altura=float(input("Dame la altura: "))
    profundidad=float(input("Dame la profundidad: "))
    arearec(base,altura)
    print("El volumen del prisma es:",volumen(area,profundidad))
area=int()
pass
