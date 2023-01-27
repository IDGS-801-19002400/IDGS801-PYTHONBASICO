
class OperasBas:

    #propiedades de clase

    n1 = 0
    n2 = 0
    res = 0

    #constructor

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


    #metodos de clase

    def suma(self):


        self.res = self.n1 + self.n2

        return self.res

        
    def resta(self):

      self.res = self.n1 - self.n2


def main():

   obj=OperasBas(3,2)
   obj.suma()
   print("La suma es: {}".format(obj.res))

   
if __name__ == '__main__':
    main()
    