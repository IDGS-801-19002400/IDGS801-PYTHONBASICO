class OperacionesBasicas:

    def __init__(self, numero1, numero2):
        
        self.numero1 = numero1
        self.numero2 = numero2

    
    def sumar (self): 

         self.res = self.numero1 + self.numero2

         return self.res

    def restar (self): 

         self.res = self.numero1 - self.numero2

         return self.res
    
    def multiplicar (self): 

         self.res = self.numero1 * self.numero2

         return self.res

    def dividir (self): 

         self.res = self.numero1 / self.numero2

         return self.res

res = 0

while res != 5:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    res = int(input("Eliga la operacion:"))


    if(res == 1):

       numero1 = int(input("Ingrese el numero 1:"))
       numero2 = int(input("Ingrese el numero 2: "))

       suma = OperacionesBasicas(numero1, numero2)
       print(suma.sumar())




    if(res == 2):

       numero1 = int(input("Ingrese el numero 1:"))
       numero2 = int(input("Ingrese el numer 2: "))

       resta = OperacionesBasicas(numero1, numero2)
       print(suma.restar())

    if(res == 3):

      numero1 = int(input("Ingrese el numero 1: "))
      numero2 = int(input("Ingrese el numero 2: "))

      multiplicacion = OperacionesBasicas(numero1, numero2)
      print("Resultados: %s %s " % suma.multiplicar())


    if(res == 4):

      numero1 = int(input("Ingrese el numero 1: "))
      numero2 = int(input("Ingrese el numero 2: "))

      division = OperacionesBasicas(numero1, numero2)
      print(suma.dividir())









   