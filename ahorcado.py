"""
Juego del Ahorcado (Hangman) en Python
Autonomo 2 - Logica de Programacion
Paso 1: Inicio del desarrollo de software

Este codigo implementa la logica descrita en los 4 diagramas de flujo
del proyecto (carpeta /diagramas):

  - Diagrama 1: flujo general del programa (funcion main)
  - Diagrama 2: detalle de jugar_una_partida()
  - Diagrama 3: detalle de actualizar_palabra_oculta()
  - Diagrama 4: funciones de validacion (letra_valida y letra_ya_usada)

Estado del avance (Paso 1): estructura completa del programa y todas las
funciones principales ya codificadas y probadas de forma manual. En los
siguientes pasos se agregaran mejoras (manejo de errores mas robusto,
mas palabras, pruebas automatizadas, etc.).
"""

import random

# Lista de palabras que puede usar el juego. Se puede ampliar mas adelante.
PALABRAS = [
    "python", "programacion", "algoritmo", "variable", "funcion",
    "computadora", "desarrollo", "software", "diagrama", "logica",
]

"""
Juego del Ahorcado (Hangman) en Python
Autonomo 2 - Logica de Programacion
 
Avance del Paso 1: interfaz de usuario e inicio del programa (Diagrama 1).
La logica completa de una partida (jugar_una_partida) se desarrolla en el
Paso 2, siguiendo el Diagrama 2.
"""
 
 
def mostrar_bienvenida():
    """
    Bloque INTERFAZ del Diagrama 1.
    Muestra el titulo del juego y una breve explicacion de las reglas,
    antes de que arranque la primera partida. Se ejecuta una sola vez,
    al inicio del programa (no se repite entre partidas).
    """
    print("=" * 40)
    print("           EL AHORCADO")
    print("=" * 40)
    print("Reglas:")
    print("- Hay una palabra oculta, letra por letra.")
    print("- En cada turno ingresas una letra.")
    print("- Tienes 6 intentos fallidos antes de perder.")
    print("=" * 40)
 
 
def jugar_una_partida():
    """
    Controla una partida completa del ahorcado (bloque detallado en el
    Diagrama 2: elegir palabra, ocultar/revelar letras, validar entradas,
    dibujar el ahorcado y detectar victoria o derrota).
 
    Pendiente de implementar: se desarrolla en el Paso 2 del proyecto.
    """
    # TODO (Paso 2): elegir_palabra(), crear_palabra_oculta(),
    # mostrar_palabra_oculta(), letra_valida(), letra_ya_usada(),
    # actualizar_palabra_oculta(), palabra_completa(), dibujar_ahorcado()
    # (ver Diagrama 2, 3 y 4).
    print("(logica de la partida pendiente para el Paso 2)")
 
 
def main():
    """
    Flujo general del programa (Diagrama 1).
 
    Orden correcto: primero se muestra la interfaz de bienvenida, luego
    se juega la primera partida sin preguntar nada, y recien despues de
    jugar se pregunta si se quiere jugar de nuevo. Si la respuesta es
    's', se vuelve directo a jugar_una_partida() (no se repite la
    bienvenida).
    """
    mostrar_bienvenida()
 
    jugar_de_nuevo = "s"
    while jugar_de_nuevo == "s":
        jugar_una_partida()
        jugar_de_nuevo = input("Jugar otra vez? (s/n): ")
        jugar_de_nuevo = jugar_de_nuevo.lower()
 
    print("Gracias por jugar!")
 
 
if __name__ == "__main__":
    main()