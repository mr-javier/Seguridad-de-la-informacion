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
        ordenClaro = 0
        if (ordenCifrado >= ord('A') and ordenCifrado <= ord('Z')):
            ordenClaro = (ordenCifrado - ord('A'))

        resultado += chr(ordenClaro)
    return resultado