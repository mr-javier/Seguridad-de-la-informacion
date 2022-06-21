# CRIPTOGRAFÍA CLÁSICA

def cifradoCesarAlfabetoInglesMAY(cadena):
    """Cifrado Cesar con desplazamiento +3, solo mayusculas"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= ord('A') and ordenClaro <= ord('Z')):
            ordenCifrado = (((ordenClaro - ord('A')) + 3) % 26) + ord('A')
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado
####################


# a) Implementar función de descifrado
def descifradoCesarAlfabetoInglesMAY(cadena):
    """Descifrado Cesar con desplazamiento +3, solo mayusculas"""
    resultado = '' 
    for c in cadena:
        ordenCifrado = ord(c)
        ordenClaro = ord(c)
        if (ordenCifrado >= ord('A') and ordenCifrado <= ord('Z')):
           ordenClaro = ((((ordenCifrado - ord('A')) + 26) - 3) % 26) + ord('A')
        resultado += chr(ordenClaro)
    return resultado

def cifradoCesarAlfabetoIngles(cadena):
    """Cifrado Cesar con desplazamiento +3, solo letras"""
    resultado = ''
    i = 0
    while i < len(cadena):
        ordenClaro = ord(cadena[i])
        ordenCifrado = ord(cadena[i]) # Para que pueda leer espacios etc.
        if (ordenClaro >= ord('A') and ordenClaro <= ord('Z')):
            ordenCifrado = (((ordenClaro - ord('A')) + 3) % 26) + ord('A')
        elif ordenClaro >= ord('a') and ordenClaro <= ord('z'):
            ordenCifrado = (((ordenClaro - ord('a')) + 3) % 26) + ord('a')
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    return resultado

def descifradoCesarAlfabetoIngles(cadena):
    """Descifrado Cesar con desplazamiento +3, solo letras"""
    resultado = '' 
    for c in cadena:
        ordenCifrado = ord(c)
        ordenClaro = ord(c)
        if (ordenCifrado >= ord('A') and ordenCifrado <= ord('Z')):
           ordenClaro = ((((ordenCifrado - ord('A')) + 26) - 3) % 26) + ord('A')
        elif ordenCifrado >= ord('a') and ordenCifrado <= ord('z'):
            ordenClaro = ((((ordenCifrado - ord('a')) + 26) - 3) % 26) + ord('a')
        resultado += chr(ordenClaro)
    return resultado

def cifradoCesar(cadena, desp):
    """
    Cifrado Cesar con desplazamiento +desp, cualquier caracter ACII
    cadena : str
    desp   : int
    """
    # TODO
    resultado = ''
    for c in cadena:
        ordenCifrado = (ord(c) + desp) % 127
        resultado += chr(ordenCifrado)
    return resultado

def descifradoCesar(cadena, desp):
    """
    Descifrado Cesar con desplazamiento +desp, cualquier caracter
    cadena : str
    desp   : int
    """
    resultado = ''
    for c in cadena:
        ordenCifrado = ((ord(c) + 127) - desp) % 127
        resultado += chr(ordenCifrado)
    return resultado


############ PRUEBAS ##############

if __name__ == "__main__":
    # a) 
    mensaje1 = "HOLA MUNDO"
    print("Mensaje: " + mensaje1)
    cifrado1 = cifradoCesarAlfabetoInglesMAY(mensaje1)
    print("Cifrado: " + cifrado1)
    claro1   = descifradoCesarAlfabetoInglesMAY(cifrado1)
    print("Descifrado: " + claro1)

    # b) Que soporte tanto mayúsculas como minúsculas
    mensaje2 = "Secret message"
    print("Mensaje: " + mensaje2)
    cifrado2 = cifradoCesarAlfabetoIngles(mensaje2)
    print("Cifrado: " + cifrado2)
    claro2 = descifradoCesarAlfabetoIngles(cifrado2)
    print("Descifrado: " + claro2)

    # c) Cesar generalizado
    mensaje3 = "Mensaje! Secreto! (Secret message...)"
    print("Mensaje: " + mensaje3)
    cifrado3 = cifradoCesar(mensaje3, 14)
    print("Cifrado: " + cifrado3)
    claro3 = descifradoCesar(cifrado3, 14)
    print("Descifrado: " + claro3)