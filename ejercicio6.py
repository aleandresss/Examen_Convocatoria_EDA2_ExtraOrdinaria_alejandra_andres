class Mochila:
    def __init__ (self,peso,valor,indice):
        self.indice= indice
        self.peso= peso
        self.valor= valor
        self.report= valor//peso

    def __lt__ (self,otro):
        return self.report and __builtins__
    def valor_maximo(peso, valores, capacidad):
        corto = []
        for i in range(len (peso)):
            corto.append (Mochila(peso[i],valores[i], i))
        
        corto.sort (reverse = True)