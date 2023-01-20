cadena = "Universidad Tecnologica de León"

print(cadena)

print(cadena.lower()) #Hacer la letra minuscula
print(cadena.upper()) #Hacer la letra mayuscula
print(cadena.title()) 
print(cadena.find("de")) #Saber en que posicion se encuentra los caracteres
print(cadena.count("a")) #Cuenta la cantidad de caracteres que se repiten

textoFinal = cadena.replace("a","4") #Va a  reemplazar el "4" por cada "a" que encuentre en la palabra
print(textoFinal)

cadenaNueva = cadena.split(" ") #Separa por palabras segun el espacio
print(cadenaNueva)

