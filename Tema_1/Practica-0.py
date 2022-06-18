import os
import json
from Crypto.Random import get_random_bytes as grb

from sympy import continued_fraction, parallel_poly_from_expr

# int(x) trunca los decimales para la conversión
# Lineas impares: *
# Lineas pares:   + 
def imprimir_piramide(altura):
    for x in range(altura):
        if x%2 == 0:
            linea = '*' * (x+1) # Ya que empieza en 0
        else:
            linea = '+' * (x+1)
        print(linea)

# EJERCICIO 3
class Piramide:
    def __init__(self, altura):
        self.altura = altura
        self.impar  = '*'
        self.par    = '+'

    def dibujar(self):
       for x in range(self.altura):
        if x%2 == 0:
            linea = self.impar * (x+1) 
        else:
            linea = self.par * (x+1)
        print(linea)

    def cambiar_estrellas(self):
        tmp        = self.impar
        self.impar = self.par
        self.par   = tmp


# EJERCICIO 4
def to_upper(cadena):
    nueva_cadena = ''
    dif = ord('A') - ord('a')
    for c in cadena:
        nc = c
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            nc = chr(ord(c) + dif)
        nueva_cadena += nc
    return nueva_cadena

def to_lower(cadena):
    nueva_cadena = ''
    dif = ord('a') - ord('A')
    for c in cadena:
        nc = c
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            nc = chr(ord(c) + dif)
        nueva_cadena += nc
    return nueva_cadena


# EJERCICIO 5
# funcion: (<bytes>, <bytes>) -> <cadena json>
# DESERIALIZAR 2 OBJETOS DE LA CLASE BYTES
def bytes2json(b1, b2):
    return json.dumps({"bytes": [b1.hex(), b2.hex()]})

#
def json2bytes(json_msg):
    msg = json.loads(json_msg)
    b1 = msg['bytes'][0].encode("utf-8")
    b2 = msg['bytes'][1].encode("utf-8")
    return b1, b2

if __name__ == "__main__":
    print("EJERCICIO 1 y 2")
    print("------------")
    imprimir_piramide(5)

    print("\nEJERCICIO 3")
    print("------------")
    piramide1 = Piramide(5)
    piramide1.dibujar()
    piramide1.cambiar_estrellas()
    piramide1.dibujar()

    print("\nEJERCICIO 4") 
    print("------------")
    print(to_upper("HolA MUnDo"))
    a = 'Asfasd Ojso oj Oj '
    b = '123!? Ab CDdD(*-+'
     
    # Comparando las funciones con las que vienen en Python:
    print(to_upper(a) == a.upper())
    print(to_upper(b) == b.upper())
    print(to_lower(a) == a.lower())
    print(to_lower(b) == b.lower())

    print("\nEJERCICIO 5") 
    print("-------------")
    b1 = grb(16)
    print(b1.hex())
    b2 = grb(16)
    print(b2.hex())

    json_msg = bytes2json(b1, b2)
    print(json_msg)

    b1, b2 = json2bytes(json_msg)
    print(b1, b2)
    print(type(b1), type(b2))