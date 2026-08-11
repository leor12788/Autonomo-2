# Ahorcado - Autonomo 2 Logica de Programacion
# Paso 2: logica principal del juego (Diagramas 2, 3 y 4)
 
import random
 
# lista de palabras posibles
PALABRAS = [
    "python", "programacion", "algoritmo", "variable", "funcion",
    "computadora", "desarrollo", "software", "diagrama", "logica",
]
 
INTENTOS_INICIALES = 6
 
# un dibujo por cada cantidad de intentos fallidos (0 a 6)
DIBUJOS_AHORCADO = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
]
 
 
def mostrar_titulo():
    # interfaz: encabezado del juego
    print("=" * 40)
    print("           EL AHORCADO")
    print("=" * 40)
 
 
def mostrar_instrucciones():
    # interfaz: reglas del juego
    print("Reglas del juego:")
    print("- Hay una palabra oculta, letra por letra.")
    print("- En cada turno ingresas una letra.")
    print("- Tienes 6 intentos fallidos antes de perder.")
    print()
 
 
def elegir_palabra():
    # elige una palabra al azar de la lista
    indice = random.randint(0, len(PALABRAS) - 1)
    return PALABRAS[indice]
 
 
def crear_palabra_oculta(palabra):
    # arma la lista de guiones, uno por cada letra
    palabra_oculta = []
    for i in range(len(palabra)):
        palabra_oculta.append("_")
    return palabra_oculta
 
 
def mostrar_palabra_oculta(palabra_oculta):
    print(" ".join(palabra_oculta))
 
 
def letra_valida(letra):
    # valida: un solo caracter y alfabetico
    if len(letra) == 1 and letra.isalpha():
        return True
    else:
        return False
 
 
def letra_ya_usada(letra, letras_usadas):
    # recorre la lista de letras usadas buscando coincidencia
    indice = 0
    while indice < len(letras_usadas):
        if letras_usadas[indice] == letra:
            return True
        indice = indice + 1
    return False
 
 
def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    # revela las posiciones donde la palabra tiene esa letra
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta
 
 
def palabra_completa(palabra_oculta):
    return "_" not in palabra_oculta
 
 
def dibujar_ahorcado(intentos_fallidos):
    print(DIBUJOS_AHORCADO[intentos_fallidos])
 
 
def jugar_una_partida():
    # una partida completa (Diagrama 2)
    palabra = elegir_palabra()
    palabra_oculta = crear_palabra_oculta(palabra)
    letras_usadas = []
    intentos = INTENTOS_INICIALES
    intentos_fallidos = 0
 
    while intentos > 0 and not palabra_completa(palabra_oculta):
        dibujar_ahorcado(intentos_fallidos)
        mostrar_palabra_oculta(palabra_oculta)
        print("Intentos restantes:", intentos)
        print("Letras usadas:", letras_usadas)
 
        letra = input("Ingresa una letra: ")
        letra = letra.lower()
 
        # letra invalida (no es una sola letra del alfabeto): pide de nuevo
        if letra_valida(letra) == False:
            print("Ingresa una sola letra valida.")
            continue
 
        # letra repetida: pide de nuevo
        if letra_ya_usada(letra, letras_usadas) == True:
            print("Ya usaste esa letra.")
            continue
 
        if letra in palabra:
            letras_usadas.append(letra)
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
        else:
            letras_usadas.append(letra)
            intentos -= 1
            intentos_fallidos += 1
            print("Fallaste...")
 
    dibujar_ahorcado(intentos_fallidos)
 
    if palabra_completa(palabra_oculta):
        print("Ganaste! La palabra era:", palabra)
    else:
        print("Perdiste. La palabra era:", palabra)
 
 
def main():
    mostrar_titulo()
    mostrar_instrucciones()
    input("Presiona ENTER para comenzar...")
 
    jugar_de_nuevo = "s"
    while jugar_de_nuevo == "s":
        jugar_una_partida()
        jugar_de_nuevo = input("Jugar otra vez? (s/n): ").lower()
 
    print("Gracias por jugar!")
 
 
if __name__ == "__main__":
    main()