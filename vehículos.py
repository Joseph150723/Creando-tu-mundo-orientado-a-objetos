class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca    
        self._modelo = modelo  
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo


    def encender(self):
        print("El vehículo está encendiendo.")

class Auto(Vehiculo):
    def encender(self):
        print(f"El auto {self.marca} modelo {self.modelo} está arrancando con llave.")

class Motocicleta(Vehiculo):
    def encender(self):
        print(f"La motocicleta {self.marca} modelo {self.modelo} está encendiendo con el botón.")

if __name__ == "__main__":
    mi_auto = Auto("Toyota", "Corolla")
    mi_moto = Motocicleta("Honda", "CBR")

    mi_auto.encender()
    mi_moto.encender()