import random 

class ArtefactosValiosos():
    def _init_(self,peso,nombre,precio,fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print('Se ha creado un artefacto')
    
    def _str_(self)
        return "Artefacto: {}, Peso: {}, Precio: {}, Fecha Caducidad: {}".format(self.nombre,self.peso,self.precio,self.fecha)