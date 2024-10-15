class Bancos:
    def __init__(self, nombre, direccion, numero_de_cuenta, saldo, tipo_de_cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
        self.tipo_de_cuenta = tipo_de_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

banco1 = Bancos("Banco del Sur", "Calle 123", "123456789", 1000, "Ahorros")
banco2 = Bancos("Banco del Norte", "Avenida Principal 456", "987654321", 2000, "Corriente")
banco3 = Bancos("Banco Central", "Plaza Mayor", "555555555", 5000, "Ahorros")

print(banco1.nombre)
print(banco2.direccion)
print(banco3.saldo)

class Reloj:
    def __init__(self):
        self.hora = self.validar_hora(int(input("Ingrese la hora (0-23): ")))
        self.minutos = self.validar_minutos(int(input("Ingrese los minutos (0-59): ")))
        self.segundos = self.validar_segundos(int(input("Ingrese los segundos (0-59): ")))
        self.alarma = input("¿Qué días se repite la alarma? ")
        self.sonido = input("Ingrese la canción para la alarma: ")
        self.almacenamiento = 1

    def validar_hora(self, hora):
        if 0 <= hora <= 23:
            return hora
        else:
            print("Hora inválida. Ingrese un valor entre 0 y 23.")
            return self.validar_hora(int(input("Ingrese la hora (0-23): ")))


    def encender(self):
        print("Encendiendo")

r1 = Reloj()
r1.encender()
r1.apagar()
r1.reiniciar()
r1.cancion()
r1.dias() 



class computador:
#atributos
marca= Hp
procesador= CPU
Discoduro= memoria
Puertos= USB
sistema operativo= linux
#metodos
def encender (self):
  print("iniciando")
def apagar (self):
  print("apagando")
def almacenamiento (self):
  print("guardando")
def entrada (self):
  print("conectando")
def salida (self):
  print("desconectando")
c1=computador()
c1.encender()
c1.apagar()
c1.almacenamiento()
c1.entrada()
c1.salida()