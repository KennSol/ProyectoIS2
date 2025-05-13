import sys
import random

def determinar_ganador(usuario, programa):
    """Determina quién gana: 1=usuario, 0=empate, -1=programa"""
    usuario = usuario.lower()
    programa = programa.lower()
    
    if usuario == programa:
        return 0
    
    if (usuario == "piedra" and programa == "tijera") or \
       (usuario == "tijera" and programa == "papel") or \
       (usuario == "papel" and programa == "piedra"):
        return 1
    else:
        return -1

def main():
    # Validar argumentos de línea de comandos
    if len(sys.argv) != 4:
        print("Uso: python juego.py <jugada1> <jugada2> <jugada3>")
        print("Ejemplo: python juego.py piedra papel tijera")
        sys.exit(1)
    
    # Obtener jugadas del usuario desde los argumentos
    usuario = sys.argv[1:4]  # Toma los 3 argumentos (jugada1, jugada2, jugada3)
    
    # Validar que las jugadas sean válidas
    opciones_validas = ["piedra", "papel", "tijera"]
    for jugada in usuario:
        if jugada.lower() not in opciones_validas:
            print(f"Error: '{jugada}' no es una jugada válida. Usa piedra, papel o tijera.")
            sys.exit(1)
    
    # Generar jugadas aleatorias del programa
    programa = [random.choice(opciones_validas) for _ in range(3)]
    
    # Mostrar jugadas del programa
    print(f"El programa elije: {' '.join(programa)}")
    
    # Comparar jugadas y calcular puntos
    puntos_usuario = 0
    puntos_programa = 0
    
    for u, p in zip(usuario, programa):
        resultado = determinar_ganador(u, p)
        if resultado == 1:
            puntos_usuario += 1
        elif resultado == -1:
            puntos_programa += 1
    
    # Mostrar puntuación
    print(f"Punteo: {puntos_usuario} – {puntos_programa}")
    
    # Determinar ganador
    if puntos_usuario > puntos_programa:
        print("Ganador: Humano")
    elif puntos_programa > puntos_usuario:
        print("Ganador: Programa")
    else:
        print("Ganador: Empate")

if __name__ == "__main__":
    main()