from abc import ABC, abstractmethod #SE IMPORTA la biblioteca "abc" para definir clases abstractas y métodos abstractos

#SE CREA LA CLASE ProfeEstudiante con los métodos esta sera la clase padre
class ProfeEstudiante(ABC):
    @abstractmethod
    def Cedula(self, cedula): #metodo abstracto cedula
        pass

    @abstractmethod
    def Nombre(self, nombre):#metodo abstracto nombre
        pass

    @abstractmethod
    def fechaNacimiento(self, fechaNacimiento):#metodo abstracto fecha de nacimiento
        pass

    @abstractmethod
    def nCelular(self, nCelular):#metodo abstracto cedula
         pass
