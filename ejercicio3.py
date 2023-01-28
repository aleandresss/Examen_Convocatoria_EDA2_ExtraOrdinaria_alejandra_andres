class armadura(object):
    nombre = ""
    rango = 0 

    def _init_(self,nombre,rango):
        self.nombre = nombre
        self.rango = rango 
        print("La armadura se ha creado con éxito")

    def calificacion(armadura):
        print(f"Código de legión: {armadura.nombre[0:2]}\n")
        print(f"Identificación ciherente: {armadura.nombre[3]}\n")
        print(f"Identificación del siglo: {armadura.nombre[4]}\n")
        print(f"Número de armadura: {armadura.nombre[5]}\n")
        print(f"Número de escuadra: {armadura.nombre[6]}\n")

    def _str_(self):
        return f"NOMBRE:\t {self.nombre}\n\n" \
            f"RANGO:\t {self.rango}\n"

    