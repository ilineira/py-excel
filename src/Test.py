from src.entidades.Workbook import Workbook
from src.entidades.Persona import Persona
import random
import string


def randomPerson(numero):
    persona = Persona({
        'Ciudad': 'A',
        'Apellido': random.choice(string.ascii_uppercase),
        'Nombre': random.choice(string.ascii_uppercase),
        'SegundoNombre': random.choice(string.ascii_uppercase),
        'Sexo': random.choice(string.ascii_uppercase),
        'Dni': numero,
        'Calle': random.choice(string.ascii_uppercase),
        'NumeroDeCalle': random.choice(string.ascii_uppercase),
        'Piso': random.choice(string.ascii_uppercase),
        'Departamento': random.choice(string.ascii_uppercase)
    })
    return persona


def main():
    workbookName = '/Users/ilineira/PycharmProjects/py-excel/output/outputCausa122692020.xlsx'
    #workbookName = '/Users/ilineira/Desktop/prueba.xlsx'
    workbook = Workbook(workbookName)
    for i in range(200):
        persona = randomPerson(i + 1)
        workbook.cargarPersona(persona)
    workbook.close()
    return


if __name__ == '__main__':
    main()
