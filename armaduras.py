#gestor de clientes
from random import randit 

class armadura(object):
    nombre = ""
    rango = ""

    def _init_ (self,nombre,rango):
        self.nombre = nombre
        self.rango = rango 
        print("La armadura se ha creado con exito")
    
    def calificacion(armadura):
        print(f"Código de legión: {armadura.nombre[0:2]}\n")
        print(f"Identificación ciherente: {armadura.nombre[3]}\n")
        print(f"Identificación del siglo: {armadura.nombre[4]}\n")
        print(f"Número de armadura: {armadura.nombre[5]}\n")
        print(f"Número de escuadra: {armadura.nombre[6]}\n")

if _name_ == "_main_":
    lista = [armadura("MK-4726",2),armadura("NR-2205",3),armadura("ST-9481",1),armadura("MK-4711",2)]
    for armadura in lista:
        calificacion(armadura)