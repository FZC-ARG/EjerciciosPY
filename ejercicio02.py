class Alumno:
    # Constructor
    def __init__(self, codigo, nombres, apellidos, nota):
        self.codigo = codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.nota = nota
    # función para imprimir los datos
    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nombres: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Nota: ", self.nota)
    # función para obtener el resultado
    def condicion(self):
        if self.nota < 14:
            print("El alumno esta desaprobado")
        else:
            print("El alumno ha aprobado")

# bloque principal
# creamos los nuevos objetos
alumno1 = Alumno("01","Apaza","Juan",12)
alumno2 = Alumno("02","Flores","Smith",15)

# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.condicion()
alumno2.imprimir()
alumno2.condicion()

class Docente:
    def __init__(self,dni,apellidos,nombres,sueldo):
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.sueldo = sueldo
        self.afp = 0
        self.seguro = 0

    # Funcion para imprimir los datos
    def imprimir(self):
        print("-------------------------------------------------")
        print("DNI: ",self.dni)
        print("Apellido: ",self.apellidos)
        print("Nombre: ",self.nombres)
        print("Sueldo: ",self.sueldo)
        print("AFP: ", self.afp)
        print("Seguro EsSalud: ", self.seguro)

    def categoria(self):
        self.afp = self.sueldo * 0.11
    
    def esSalud(self):
        self.seguro = self.sueldo * 0.02

docente1 = Docente("71340256","Alvares","Francisco",1200)
docente1.categoria()
docente1.esSalud()
docente1.imprimir()

