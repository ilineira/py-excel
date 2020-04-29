from src.entidades.Workbook import Workbook
from src.entidades.Persona import Persona


def main():
    workbookName = '/Users/ilineira/PycharmProjects/py-excel/output/outputCausa122692020.xlsx'
    #workbookName = '/Users/ilineira/Desktop/prueba.xlsx'
    workbook = Workbook(workbookName)
    persona = Persona({
        'Ciudad': 'a',
        'Apellido': 'a',
        'Nombre': 'a',
        'SegundoNombre': 'a',
        'Sexo': 'a',
        'Dni': 'a',
        'Calle': 'a',
        'NumeroDeCalle': 'a',
        'Piso': 'a',
        'Departamento': 'a'
    })
    persona2 = Persona({
        'Ciudad': 'a',
        'Apellido': 'b',
        'Nombre': 'b',
        'SegundoNombre': 'b',
        'Sexo': 'b',
        'Dni': 'b',
        'Calle': 'b',
        'NumeroDeCalle': 'b',
        'Piso': 'b',
        'Departamento': 'b'
    })
    workbook.cargarPersona(persona)
    workbook.cargarPersona(persona2)
    workbook.close()
    return


if __name__ == '__main__':
    main()