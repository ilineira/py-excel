from src.entidades.Workbook import Workbook
from src.entidades.Persona import Persona


class CargadorAExcel:

    def __init__(self, rutaAArchivo):
        self.continuar = True
        self.workbook = Workbook(rutaAArchivo)

    def run(self):
        while self.continuar:
            self.cargarPersona()
            self.deseaContinuar()

    def deseaContinuar(self):
        if input('Desea continuar?') is 0:
            self.workbook.close()
            self.continuar = False

    def cargarPersona(self):
        print('Cargar dato y presionar enter para continuar con el siguiente campo')
        persona = Persona({
            'Ciudad': input('Ingresar ciudad: '),
            'Apellido': input('Ingresar apellido: '),
            'Nombre': input('Ingresar nombre: '),
            'SegundoNombre': input('Ingresar segundo nombre: '),
            'Sexo': input('Ingresar sexo: '),
            'Dni': input('Ingresar DNI: '),
            'Calle': input('Ingresar calle: '),
            'NumeroDeCalle': input('Ingresar numero de calle: '),
            'Piso': input('Ingresar piso: '),
            'Departamento': input('Ingresar departamento: ')
        })
        self.workbook.cargarPersona(persona)
