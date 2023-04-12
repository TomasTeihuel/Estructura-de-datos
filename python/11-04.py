# otro codigo en tarea.py 
#escribir un porgrama que le pida al usuario una palabra y muestre por consola el n° de veces que contiene cada vocal 
cadena = "abuelito"
def contar_vocales(cadena):
	contador_a = 0
	contador_e = 0
	contador_i = 0
	contador_o = 0
	contador_u = 0
	for letra in cadena:
		if letra.lower() in "a":
			contador_a += 1
	for letra in cadena:
		if letra.lower() in "e":
			contador_e += 1
	for letra in cadena:
		if letra.lower() in "i":
			contador_i += 1
	for letra in cadena:
		if letra.lower() in "o":
			contador_o += 1
	for letra in cadena:
		if letra.lower() in "u":
			contador_u += 1
	return contador_a, contador_e,contador_i,contador_o,contador_u
#print("la palabra tiene", contador_a,"a", contador_e, "e",contador_i, "i",contador_o, "o",contador_u, "u")
print("las vocales a-e-i-o-u estan en ese orden")
print(contar_vocales(cadena))