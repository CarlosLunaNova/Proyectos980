

class Estudiante(object):
    def __init__(self, carnet, nombre, cursos=[]):
        self.carnet = carnet
        self.nombre = nombre
        self.cursos = cursos

    def getCarnet(self):
        return self.carnet

    def getNombre(self):
        return self.nombre
    
    def getCursos(self):
        a=[]
        for i in self.cursos:
            a.append(i)
        return a
    
    def contCursos(self):
        return len(self.getCursos())

    def addCurso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        return str('Yo soy :'+ self.getNombre())

    def __repr__(self):
        return self.__str__()

    