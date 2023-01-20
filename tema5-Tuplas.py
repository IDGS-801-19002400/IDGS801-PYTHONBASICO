#La tuplas son estaticas no permiten cambios

tupla = (1,2,3) #Esta es una tupla con 3 elementos
print(tupla)
print(type(tupla))

tupla2 = (7, "Roberto", True, 23.8, 16+7)
print(tupla2)

print(tupla2[1])

print(tupla2[4])

print(tupla2[-1]) #Muestre el ultimo elemento 

print(tupla2[0:3])  #Imprime segun el rango

print(tupla2[3:]) #Imprime de la posicion 3 en adelante

a,b,c = tupla
print(a)
print(c)

tuplaN = tupla + tupla2
print(tuplaN)
print(tupla.count(2)) #Permite contar el numero de apariciones de un elemento




