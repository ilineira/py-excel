class Persona:

    def __init__(self, dictionary):
        self.ciudad = dictionary['Ciudad']
        self.apellido = dictionary['Apellido']
        self.nombre = dictionary['Nombre']
        self.segundoNombre = dictionary['SegundoNombre']
        self.sexo = dictionary['Sexo']
        self.dni = dictionary['Dni']
        self.calle = dictionary['Calle']
        self.numeroDeCalle = dictionary['NumeroDeCalle']
        self.piso = dictionary['Piso']
        self.departamento = dictionary['Departamento']

    def getCiudad(self):
        return self.ciudad

    def getApellido(self):
        return self.apellido

    def getNombre(self):
        return self.nombre

    def getSegundoNombre(self):
        return self.segundoNombre

    def getSexo(self):
        return self.sexo

    def getDni(self):
        return self.dni

    def getCalle(self):
        return self.calle

    def getNumeroDeCalle(self):
        return self.numeroDeCalle

    def getPiso(self):
        return self.piso

    def getDepartamento(self):
        return self.departamento