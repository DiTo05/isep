def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

texto1 = "Hola, esto es una cadena de texto."
texto2 = "Prueba 3"
texto3 = "Esta cadena tiene   múltiples  espacios   entre algunas palabras."

print(contar_palabras(texto1))
print(contar_palabras(texto2))
print(contar_palabras(texto3))
