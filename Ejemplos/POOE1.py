
# Funcion --> Metodo
# Variable --> Atributo

# Clase tipo Fecha
class Fecha(object):
    #Constructor
    def __init__(self, dia, mes, anio):
        # Crear variables globales dentro de la clase
        # con la informacion que era local dentro
        # del metodo constructor
        self.day = dia
        self.month = mes
        self.year = anio
    
    #Devolver la fecha como una tupla
    def mostrarFecha(self):
        x = (self.day,self.month,self.year)
        return x
    
    #Cambiar la fecha guardada
    def cambiarFecha(self, dia, mes, anio):
        self.day = dia
        self.month = mes
        self.year = anio

    # Redefine la conversion del objeto a string   
    def __str__(self):
        return str(str(self.day)+"/"+str(self.month)+"/"+str(self.year))

    # Devuelve la representacion haciendo una sobrecarga de operador
    def __repr__(self):
        return self.__str__()        

miCumple = Fecha(11,12,1997)
revolucion = Fecha(20,10,1944)
independencia = Fecha(15,9,1821)