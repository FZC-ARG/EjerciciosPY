import math
class Calculadora:
    #INICIALIZAR CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.nro1 = int(input("Ingrese el valor del nro1: "))
        self.nro2 = int(input("Ingrese el valor del nro2: "))
    
    #FUNCION PARA SUMAR
    def sumar(self):
        suma = self.nro1 + self.nro2
        print("El resultado de la suma es: ", suma)
    
    #FUNCION PARA RESTAR
    def restar(self):
        resta = self.nro1 - self.nro2
        print("El resultado de la resta es: ", resta)

    #FUNCION PARA MULTIPLICAR
    def multiplicar(self):
        multiplicacion = self.nro1 * self.nro2
        print("El resultado de la multiplicación es: ", multiplicacion)
    
    #FUNCION PARA DIVIDIR
    def dividir(self):
        division = self.nro1 / self.nro2
        print("El resultado de la division es: ", division)
    
    #FUNCION PARA POTENCIA
    def potenciar(self):
        potencia=1.
        for i in range(0,self.nro2):
            potencia = potencia*self.nro1
        print("El resultado de la potencia es: ", potencia)
    
    #FUNCION PARA FACTORIAL
    def factorial(self):
        fact =1
        for i in range(1,self.nro1+1):
            fact = fact*i
        print("El factorial de ",self.nro1,"es: ", fact)
        fact = 1
        for i in range(1,self.nro2+1):
            fact = fact*i
        print("El factorial de ",self.nro2,"es: ", fact)
    
    
    #FUNCION PARA RAIZ
    def racionalizar(self):
        racionalizacion = math.sqrt(self.nro1)
        print("La raiz de ",self.nro1,"es: ", racionalizacion)
        racionalizacion = math.sqrt(self.nro2)
        print("La raiz de ",self.nro2,"es: ", racionalizacion)

    #FUNCION PARA IMPRIMIR LOS RESULTADOS
    def imprimir(self):
        print("Los valores son: ")
        print("Nro1: ",self.nro1)
        print("Nro2: ",self.nro2)

calcular = Calculadora()
calcular.imprimir()
calcular.sumar()
calcular.restar()
calcular.multiplicar()
calcular.dividir()
calcular.potenciar()
calcular.factorial()
calcular.racionalizar()

    