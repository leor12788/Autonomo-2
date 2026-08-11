# Ahorcado - Autonomo 2 Logica de Programacion
# Avance Paso 1: interfaz de usuario (Diagrama 1)
 
 
def mostrar_titulo():
    print("=" * 40)
    print("           EL AHORCADO")
    print("=" * 40)
 
 
def mostrar_instrucciones():
    print("Reglas del juego:")
    print("- Hay una palabra oculta, letra por letra.")
    print("- En cada turno ingresas una letra.")
    print("- Tienes 6 intentos fallidos antes de perder.")
    print()
 
 
def main():
    mostrar_titulo()
    mostrar_instrucciones()
    input("Presiona ENTER para comenzar...")
 
 
if __name__ == "__main__":
    main()