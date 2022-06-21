# CRIPTOGRAFÍA CLÁSICA

# DADO EL SIGUIENTE CÓDIGO:
def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
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
    resultado = '' 
    for c in cadena:
        ordenCifrado = ord(c)
        ordenClaro = ord(c)
        if (ordenCifrado >= ord('A') and ordenCifrado <= ord('Z')):
           ordenClaro = ((((ordenCifrado - ord('A')) + 26) - 3) % 26) + ord('A')
        resultado += chr(ordenClaro)
    return resultado

def cifradoCesarAlfabetoIngles(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
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