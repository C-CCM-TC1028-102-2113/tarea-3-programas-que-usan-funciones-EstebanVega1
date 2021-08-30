año = int(input("Introduzca año:"))

print("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) else "No es bisiesto")
def es_bisiesto(año):
	return not año % 4 and (año % 100 or not año % 400)
