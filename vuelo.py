# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Vuelo(object):
    
    def __init__(self, numero_vuelo, id_vuelo, origen, destino, hora_salida, hora_llegada):
        
        self.numero_vuelo = numero_vuelo
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
    

    def __str__(self):
        
        coma = ","
        return "(" + str(self.numero_vuelo) + coma + str(self.id_vuelo) + coma + str(self.origen) + coma + str(self.destino) + coma + str(self.hora_salida) + coma + str(self.hora_llegada) + ")"
        